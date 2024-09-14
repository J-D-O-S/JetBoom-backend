from django.db import models
from Usuarios.models import Usuario


class FidelizacionModel(models.Model):
    opinion_servicio = models.CharField(
        max_length=1000, verbose_name="Opinion del servicio"
    )

    TIPOS_SOLICITUD = [
        ("", "Seleccione su solicitud"),
        ("p", "Petición"),
        ("q", "Queja"),
        ("r", "Reclamo"),
        ("s", "Sugerencia"),
        ("f", "Felicitacion"),
    ]

    tipo_solicitud = models.CharField(
        max_length=1,
        choices=TIPOS_SOLICITUD,
        default="",
        verbose_name="Tipo de solicitud",
        default="",
    )
    archivo_adjunto = models.FileField(
        upload_to="Fidelizacion/archivos_adjuntos/",
        verbose_name="Archivo adjunto",
        blank=True,
        null=True,
    )
    archivo_adjunto = models.FileField(
        upload_to="Fidelizacion/archivos_adjuntos/",
        blank=True,
        null=True,
        verbose_name="Archivo adjunto",
    )
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)


class Reto(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre del reto")
    descripcion = models.CharField(max_length=1000, verbose_name="Descripción del reto")
    fecha_inicio = models.DateField(verbose_name="Fecha de inicio")
    fecha_fin = models.DateField(verbose_name="Fecha de finalización")
    punto_por_ganar = models.IntegerField(verbose_name="Puntos por ganar")
    imagen = models.ImageField(
        upload_to="Fidelizacion/retos/", verbose_name="Imagen del reto"
    )
    is_active = models.BooleanField(default=True, verbose_name="Reto activo")
    reto_completado = models.BooleanField(default=False, verbose_name="Reto completado")
    usuario_participante = models.ManyToManyField(
        Usuario, related_name="reto", verbose_name="Usuarios participantes"
    )

    def __str__(self):
        return self.nombre
