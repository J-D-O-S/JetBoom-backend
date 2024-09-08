from django.db import models
from Usuarios.models import Usuario


class Fidelizacion(models.Model):
    opinion_servicio = models.CharField(
        max_length=1000, verbose_name="Opinion del servicio"
    )

    TIPOS_SOLICITUD = [
        ("", "Seleccione su solicitud"),
        ("p", "Pregunta"),
        ("q", "Queja"),
        ("r", "Reclamo"),
        ("s", "Sugerencia"),
        ("f", "Felicitacion"),
    ]

    tipo_solicitud = models.CharField(
        max_length=1,
        choices=TIPOS_SOLICITUD,
        verbose_name="Tipo de solicitud",
    )

    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
