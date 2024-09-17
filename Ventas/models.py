from django.db import models


class Ventas(models.Model):
    fecha_hora_venta = models.DateTimeField(
        auto_now_add=True, verbose_name="Fecha de venta"
    )
    total = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="Total de la venta"
    )
    OPCIONES_FORMAS_PAGO = [
        ("", "Seleccine una forma de pago"),
        ("pse", "PSE"),
        ("pyu", "PayU"),
    ]

    forma_pago = models.CharField(
        max_length=3,
        choices=OPCIONES_FORMAS_PAGO,
        default="",
        verbose_name="Forma de pago",
    )

    usuario = models.ForeignKey("Usuarios.Usuario", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.usuario} {self.total}"


class DetalleComprobantePago(models.Model):
    cantidad_personas = models.IntegerField(
        default=1, verbose_name="Cantidad de personas que beneficiarias del servicio"
    )
    valor_unitario_servicio = models.DecimalField(
        max_digits=20, decimal_places=2, verbose_name="Valor unitario del servicio"
    )
    valor_guia = models.DecimalField(
        max_digits=20, decimal_places=2, default=60000, verbose_name="Valor del guía"
    )
    comision_servicio = models.DecimalField(
        max_digits=20, decimal_places=2, verbose_name="Comisión del servicio"
    )
    valor_total_servicio = models.DecimalField(
        max_digits=20, decimal_places=2, verbose_name="Valor total del servicio"
    )
    ventas = models.OneToOneField(Ventas, on_delete=models.CASCADE)
    servicios = models.ForeignKey("Servicios.Servicios", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.servicios} {self.ventas}"


class Reserva(models.Model):
    fecha_hora_reserva = models.DateTimeField(verbose_name="Fecha y hora de reserva")
    cantidad_personas = models.IntegerField(
        default=1, verbose_name="Cantidad de personas"
    )

    OPCIONES_ESTADO_RESERVA = [
        ("p", "pendiente"),
        ("e", "Ejecutada"),
    ]

    estado_reserva = models.CharField(
        max_length=1,
        choices=OPCIONES_ESTADO_RESERVA,
        default="a",
        verbose_name="Estado de reserva",
    )

    ventas = models.OneToOneField(Ventas, on_delete=models.CASCADE)
    servicios = models.ForeignKey("Servicios.Servicios", on_delete=models.CASCADE)

    def __str__(self):
        return (
            f"{self.estado_reserva} {self.fecha_hora_reserva} {self.cantidad_personas}"
        )
