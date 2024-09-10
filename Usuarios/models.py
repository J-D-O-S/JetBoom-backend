import os
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
        upload_to="static/images/perfil/",
        max_length=200,
        blank=True,
        null=True,
    )
    numero_identificacion = models.CharField(
        max_length=20, verbose_name="Número de Identificación"
    )

    TIPO_IDENTIFICACION_CHOICES = [
        ("", "Seleccione su identificación"),
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
        return f"Nombre completo: {self.nombre} {self.segundo_nombre} {self.apellido} {self.segundo_apellido}\nEmail: {self.email}"

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    def save(self, *args, **kwargs):
        if self.pk and self.foto_perfil:
            try:
                old_foto = Usuario.objects.get(pk=self.pk).foto_perfil
                if old_foto and old_foto.url != self.foto_perfil.url:
                    if os.path.isfile(old_foto.path):
                        os.remove(old_foto.path)
            except Usuario.DoesNotExist:
                pass  # El objeto es nuevo, por lo que no hay foto antigua para eliminar

        super(Usuario, self).save(*args, **kwargs)


# codigo de ChatGPT


# Modelo para EstadoFoto
# class EstadoFoto(models.Model):
#     nombreEstado = models.CharField(max_length=20)


# # Modelo para Foto
# class Foto(models.Model):
#     descripcionFoto = models.CharField(max_length=100)
#     foto = models.ImageField(upload_to="fotos/")
#     comentarioAdmin = models.CharField(max_length=500)
#     fechaCreacion = models.DateTimeField(auto_now_add=True)
#     usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
#     estadoFoto = models.ForeignKey(EstadoFoto, on_delete=models.CASCADE)


# # Modelo para EstadoReto
# class EstadoReto(models.Model):
#     idEstadoReto = models.AutoField(primary_key=True)
#     nombreEstado = models.CharField(max_length=20)


# # Modelo para Reto
# class Reto(models.Model):
#     idReto = models.AutoField(primary_key=True)
#     nombreReto = models.CharField(max_length=45)
#     descripcionReto = models.CharField(max_length=1000)
#     fechaInicioReto = models.DateTimeField()
#     fechaFinReto = models.DateTimeField()
#     fotoReto = models.ForeignKey(Foto, on_delete=models.CASCADE)
#     estadoReto = models.ForeignKey(EstadoReto, on_delete=models.CASCADE)


# # Modelo para TipoDocumento
# class TipoDocumento(models.Model):
#     idTipoDocumento = models.AutoField(primary_key=True)
#     tipoDocumento = models.CharField(max_length=2)


# # Modelo para UsuarioReto
# class UsuarioReto(models.Model):
#     usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
#     reto = models.ForeignKey(Reto, on_delete=models.CASCADE)
#     fecha = models.DateTimeField(auto_now_add=True)


# # Modelo para GuiaTuristico
# class GuiaTuristico(models.Model):
#     idGuiaTuristico = models.AutoField(primary_key=True)
#     nombrePrimario = models.CharField(max_length=45)
#     nombreSecundario = models.CharField(max_length=45)
#     numeroDocumento = models.CharField(max_length=20)
#     tipoDocumento = models.ForeignKey(TipoDocumento, on_delete=models.CASCADE)
#     disponibilidadGuia = models.BooleanField()


# # Modelo para MedioContacto
# class MedioContacto(models.Model):
#     idMedioContacto = models.AutoField(primary_key=True)
#     email = models.EmailField()
#     nombre = models.CharField(max_length=45)
#     usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
#     guiaTuristico = models.ForeignKey(GuiaTuristico, on_delete=models.CASCADE)


# # Modelo para Servicio
# class Servicio(models.Model):
#     idServicio = models.AutoField(primary_key=True)
#     nombreServicio = models.CharField(max_length=100)
#     descripcionServicio = models.CharField(max_length=1000)
#     fechaCreacion = models.DateTimeField(auto_now_add=True)
#     usuarioCreador = models.ForeignKey(Usuario, on_delete=models.CASCADE)
#     guiaTuristico = models.ForeignKey(GuiaTuristico, on_delete=models.CASCADE)


# # Modelo para DisponibilidadServicio
# class DisponibilidadServicio(models.Model):
#     idDisponibilidadServicio = models.AutoField(primary_key=True)
#     disponibilidad = models.CharField(max_length=45)
#     servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)


# # Modelo para EstadoReserva
# class EstadoReserva(models.Model):
#     idEstadoReserva = models.AutoField(primary_key=True)
#     nombreEstado = models.CharField(max_length=20)


# # Modelo para Reserva
# class Reserva(models.Model):
#     idReserva = models.AutoField(primary_key=True)
#     fechaHoraReserva = models.DateTimeField()
#     estadoReserva = models.ForeignKey(EstadoReserva, on_delete=models.CASCADE)
#     disponibilidadServicio = models.ForeignKey(
#         DisponibilidadServicio, on_delete=models.CASCADE
#     )


# # Modelo para FormasPago
# class FormasPago(models.Model):
#     idFormasPago = models.AutoField(primary_key=True)
#     nombreFormaPago = models.CharField(max_length=45)


# # Modelo para Venta
# class Venta(models.Model):
#     idVenta = models.AutoField(primary_key=True)
#     fechaVenta = models.DateField()
#     pagosServicio = models.FloatField()
#     registrosVentas = models.CharField(max_length=45)
#     usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
#     guiaTuristico = models.ForeignKey(GuiaTuristico, on_delete=models.CASCADE)
#     formasPago = models.ForeignKey(FormasPago, on_delete=models.CASCADE)


# # Modelo para ComprobantePago
# class ComprobantePago(models.Model):
#     idComprobantePago = models.AutoField(primary_key=True)
#     fechaHoraEmision = models.DateTimeField()
#     venta = models.ForeignKey(Venta, on_delete=models.CASCADE)
#     reserva = models.ForeignKey(Reserva, on_delete=models.CASCADE)
#     formasPago = models.ForeignKey(FormasPago, on_delete=models.CASCADE)


# # Modelo para DetalleComprobantePago
# class DetalleComprobantePago(models.Model):
#     idDetalleComprobantePago = models.AutoField(primary_key=True)
#     cantidadServicios = models.IntegerField()
#     valorUnitario = models.FloatField()
#     comprobantePago = models.ForeignKey(ComprobantePago, on_delete=models.CASCADE)
