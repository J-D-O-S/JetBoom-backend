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
        verbose_name="Tipo de solicitud",
        default="",
    )
    archivo_adjunto = models.FileField(
        upload_to="Fidelizacion/archivos_adjuntos/",
        verbose_name="Archivo adjunto",
        blank=True,
        null=True,
    )

    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
