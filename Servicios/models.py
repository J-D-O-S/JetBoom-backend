from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class GuiaTuristico(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre del guía turístico")
    apellido = models.CharField(
        max_length=100, verbose_name="Apellido del guía turístico"
    )
    numero_documento = models.CharField(
        max_length=100, verbose_name="Número de documento"
    )
    precio = models.DecimalField(
        max_digits=20,
        decimal_places=2,
        default=60000,
        verbose_name="Precio del guía turístico",
    )
    telefono = models.CharField(
        max_length=100, verbose_name="Teléfono del guía turístico"
    )
    email = models.EmailField(
        unique=True,
        max_length=254,
        verbose_name="Correo electrónico del guía turístico",
    )
    imagen = models.ImageField(
        upload_to="Servicios/guia_turistico/", verbose_name="Imagen del guía turístico"
    )
    disponibilidad = models.BooleanField(
        default=True, verbose_name="Disponibilidad del guía turístico"
    )

    def __str__(self):
        return self.nombre


class Servicios(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre del servicio")
    descripcion = models.CharField(
        max_length=1000, verbose_name="Descripción del servicio"
    )
    hora_inicio = models.TimeField(verbose_name="Hora de inicio")
    hora_fin = models.TimeField(verbose_name="Hora de finalización")
    ubicacion = models.CharField(max_length=200, verbose_name="Ubicación del servicio")
    cantidad_personas_max = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        verbose_name="Cantidad de personas máxima",
    )
    precio = models.DecimalField(
        max_digits=20, decimal_places=2, verbose_name="Precio del servicio"
    )
    imagen = models.ImageField(
        upload_to="Servicios/lugares_turisticos/", verbose_name="Imagen del servicio"
    )
    estado_disponibilidad = models.BooleanField(
        default=True, verbose_name="Estado de disponibilidad"
    )
    is_active = models.BooleanField(default=True, verbose_name="Activo")
    guia_turistico = models.ForeignKey(GuiaTuristico, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
