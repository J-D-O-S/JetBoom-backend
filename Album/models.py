import os
from django.db import models
from django.conf import settings


class AlbumFoto(models.Model):
    foto_portada = models.ImageField(
        upload_to="portada_img/",
        null=True,
        blank=True,
        verbose_name="Foto de portada",
    )
    usuario = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nombre_album = models.CharField(
        max_length=50, default="JetBoom", verbose_name="Nombre del album"
    )
    descripcion = models.TextField(
        max_length=500,
        default="Este es tú album de fotos, dónde podras almacenar todas tus historias. ¡Disfrútalo!",
        verbose_name="Descripción del album",
    )

    def __str__(self):
        return f"{self.id} {self.nombre_album}"

    def save(self, *args, **kwargs):
        if self.pk and self.foto_portada:
            try:
                old_foto = AlbumFoto.objects.get(pk=self.pk).foto_portada
                if old_foto and old_foto.url != self.foto_portada.url:
                    if os.path.isfile(old_foto.path):
                        os.remove(old_foto.path)
            except AlbumFoto.DoesNotExist:
                pass  # El objeto es nuevo, por lo que no hay foto antigua para eliminar

        super(AlbumFoto, self).save(*args, **kwargs)


class Foto(models.Model):
    album = models.ForeignKey(AlbumFoto, on_delete=models.CASCADE)
    descripcion = models.CharField(
        max_length=255,
        default="Imagen para el album",
        blank=True,
        null=True,
        verbose_name="Descripción de la imagen",
    )
    imagen = models.ImageField(upload_to="galeria_img/", verbose_name="Imagen")
    fecha = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de subida")
    comentario_publico = models.CharField(
        max_length=500, blank=True, null=True, verbose_name="Comentario público"
    )

    def __str__(self):
        return f"Album: {self.album} imagen_id: {self.id}"
