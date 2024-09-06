from django.db import models
from Usuarios.models import Usuario


# class Album(models.Model):
#     descripcion = models.CharField(max_length=1000)
#     portada = models.ImageField(upload_to="portadas/", null=True, blank=True)

#     def __str__(self):
#         return self.descripcion


# class Foto(models.Model):
#     descripcion = models.CharField(max_length=1000)
#     imagen = models.ImageField(upload_to="Usuarios/fotos/")
#     comentario = models.CharField(max_length=500)
#     album = models.ForeignKey(Album, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.descripcion


class Album(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    nombre_album = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre_album


class Foto(models.Model):
    descripcion = models.CharField(max_length=255)
    imagen = models.ImageField(upload_to="Usuarios/fotos/")
    fecha = models.DateTimeField(auto_now_add=True)
    comentario_publico = models.CharField(max_length=500, blank=True)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)

    def __str__(self):
        return self.descripcion
