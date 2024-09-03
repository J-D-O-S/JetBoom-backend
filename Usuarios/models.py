from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)


class CustomUserManager(BaseUserManager):
    def create_user(
        self,
        email,
        nombre,
        apellido,
        numero_identificacion,
        tipo_identificacion,
        password=None,
        **extra_fields,
    ):
        if not email:
            raise ValueError("El usuario debe tener un email")
        if not nombre:
            raise ValueError("El usuario debe tener un nombre")
        if not apellido:
            raise ValueError("El usuario debe tener un apellido")
        if not numero_identificacion:
            raise ValueError("El usuario debe tener un número de identificación")
        if not tipo_identificacion:
            raise ValueError("El usuario debe tener un tipo de documento")

        email_normalizado = self.normalize_email(email)
        user = self.model(
            email=email_normalizado,
            nombre=nombre,
            apellido=apellido,
            numero_identificacion=numero_identificacion,
            tipo_identificacion=tipo_identificacion,
            **extra_fields,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(
        self,
        email,
        nombre,
        apellido,
        numero_identificacion,
        tipo_identificacion,
        password=None,
        **extra_fields,
    ):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser debe tener is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser debe tener is_superuser=True.")

        return self.create_user(
            email,
            nombre,
            apellido,
            numero_identificacion,
            tipo_identificacion,
            password,
            **extra_fields,
        )


class Usuario(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, verbose_name="Correo Electrónico")
    nombre = models.CharField(max_length=20, verbose_name="Nombre")
    segundo_nombre = models.CharField(
        max_length=20, blank=True, null=True, verbose_name="Segundo Nombre"
    )
    apellido = models.CharField(max_length=20, verbose_name="Apellido")
    segundo_apellido = models.CharField(
        max_length=20, blank=True, null=True, verbose_name="Segundo Apellido"
    )
    contrasena = models.CharField(max_length=100, verbose_name="Contraseña")
    puntos_ganados = models.IntegerField(default=0, verbose_name="Puntos Ganados")
    fecha_nacimiento = models.DateField(verbose_name="Fecha de Nacimiento")
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name="Creado")
    fecha_modificacion = models.DateTimeField(auto_now=True, verbose_name="Modificado")
    foto_perfil = models.ImageField(
        "Foto de Perfil",
        upload_to="fotos_perfil/",
        max_length=200,
        blank=True,
        null=True,
    )
    numero_identificacion = models.CharField(
        max_length=20, verbose_name="Número de Identificación"
    )

    TIPO_IDENTIFICACION_CHOICES = [
        ("CC", "Cédula de Ciudadanía"),
        ("CE", "Cédula de Extranjería"),
        ("PA", "Pasaporte"),
    ]

    tipo_identificacion = models.CharField(
        max_length=2,
        choices=TIPO_IDENTIFICACION_CHOICES,
        verbose_name="Tipo de Identificación",
    )

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = [
        "nombre",
        "segundo_nombre",
        "apellido",
        "segundo_apellido",
        "fecha_nacimiento",
        "numero_identificacion",
        "tipo_identificacion",
    ]

    def __str__(self):
        return f"Nombre completo: {self.nombre} {self.segundo_nombre} {self.apellido} {self.segundo_apellido}\n Email: {self.email}\n Fecha de Nacimiento: {self.fecha_nacimiento}\n Número de Identificación: {self.numero_identificacion}\n Tipo de Identificación: {self.tipo_identificacion}"

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
