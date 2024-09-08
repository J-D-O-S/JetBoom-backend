# from django.db import models
# from Servicios.models import Servicios


# class Ventas(models.Model):
#     fecha = models.DateField()
#     monto = models.DecimalField(max_digits=10, decimal_places=2)
#     servicio = models.CharField(max_length=100)
#     cantidad = models.IntegerField()
#     total = models.DecimalField(max_digits=10, decimal_places=2)
#     cliente = models.CharField(max_length=100)

#     def __str__(self):
#         return self.cliente


# class ComprobantePago(models.Model):
#     fecha = models.DateField()
#     monto = models.DecimalField(max_digits=10, decimal_places=2)
#     # servicios = models.ForeignKey(
#     #     "Servicios.Servicios", verbose_name=_(""), on_delete=models.CASCADE
#     # )
#     # servicios = models.ForeignKey(Servicios, on_delete=models.CASCADE)

#     TIPO_FORMAS_PAGO = [
#         ("Efectivo", "Efectivo"),
#         ("Tarjeta", "Tarjeta"),
#         ("Transferencia", "Transferencia"),
#     ]

#     formas_pago = models.CharField(
#         choices=TIPO_FORMAS_PAGO,
#         verbose_name="Tipo de Identificación",
#     )
#     # comprobante = models.ImageField(upload_to="comprobantes/")

#     def __str__(self):
#         return self.cliente


# class DetalleComprobantePago(models.Model):
#     comprobante_pago = models.ForeignKey(ComprobantePago, on_delete=models.CASCADE)
#     # venta = models.ForeignKey(Ventas, on_delete=models.CASCADE)
#     cantidad_personas = models.IntegerField(default=1)
#     valor_unitario = models.DecimalField(max_digits=10, decimal_places=2)
#     total = models.DecimalField(max_digits=10, decimal_places=2)

#     def __str__(self):
#         return self.comprobante_pago.cliente
