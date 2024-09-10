from django.db import models
from django.conf import settings

# from Usuarios.models import Usuario


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


class AlbumFoto(models.Model):
    foto_portada = models.ImageField(
        upload_to="static/images/portada/", null=True, blank=True
    )
    usuario = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nombre_album = models.CharField(max_length=50, default="JetBoom")
    descripcion = models.TextField(
        max_length=500,
        default="Este es tú album de fotos, dónde podras almacenar todas mis historias. ¡Disfrútalo!",
    )

    def __str__(self):
        return f"{self.id} {self.nombre_album}"


class Foto(models.Model):
    album = models.ForeignKey(AlbumFoto, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=255)
    imagen = models.ImageField(upload_to="static/images/photos/")
    fecha = models.DateTimeField(auto_now_add=True)
    comentario_publico = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return self.descripcion
