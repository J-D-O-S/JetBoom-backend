# from django.db import models
# from django.core.validators import MinValueValidator, MaxValueValidator
# from Ventas.models import ComprobantePago


# class EstadoReserva(models.Model):
#     nombre = models.CharField(max_length=50)

#     def __str__(self):
#         return self.nombre


# class Disponibilidad(models.Model):
#     disponible = models.BooleanField(default=True)

#     def __str__(self):
#         return self.disponible


# class Servicios(models.Model):
#     nombre = models.CharField(max_length=100)
#     descripcion = models.CharField(max_length=1000)
#     hora_inicio = models.TimeField()
#     hora_fin = models.TimeField()
#     ubicacion = models.CharField(max_length=200)
#     cantidad_personas_max = models.IntegerField(
#         validators=[MinValueValidator(1), MaxValueValidator(5)]
#     )
#     precio = models.DecimalField(max_digits=10, decimal_places=2)
#     imagen = models.ImageField(upload_to="servicios/")
#     disponibilidad = models.ForeignKey(Disponibilidad, on_delete=models.CASCADE)

#     is_active = models.BooleanField(default=True)

#     def __str__(self):
#         return self.nombre


# class Reserva(models.Model):
#     fecha = models.DateField()
#     hora = models.TimeField()
#     cantidad_personas = models.IntegerField(
#         validators=[MinValueValidator(1), MaxValueValidator(5)]
#     )
#     estado = models.ForeignKey(EstadoReserva, on_delete=models.CASCADE)
#     disponibilidad = models.ForeignKey(Disponibilidad, on_delete=models.CASCADE)
#     # servicio = models.ForeignKey(Servicios, on_delete=models.CASCADE)
#     comprobante_pago = models.ForeignKey(ComprobantePago, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.cliente.nombre
