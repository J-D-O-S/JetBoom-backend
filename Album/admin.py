from django.contrib import admin

# from django.contrib.auth.admin import UserAdmin
# from .models import AlbumFoto, Foto
from .models import AlbumFoto
from .forms import CustomAlbumForm

# from django.contrib import admin
# from .models import AlbumFoto


class CustomAlbumAdmin(admin.ModelAdmin):
    add_form = CustomAlbumForm
    form = CustomAlbumForm
    model = AlbumFoto
    pass


admin.site.register(AlbumFoto, CustomAlbumAdmin)


# @admin.register(AlbumFoto)
# class CustomAlbumAdmin(UserAdmin):
#     pass
#     # list_display = ["nombre", "descripcion", "fecha_creacion", "fecha_modificacion"]
#     # search_fields = ["nombre", "descripcion"]
#     # ordering = ["nombre"]


# @admin.register(Foto)
# class CustomFotoAdmin(UserAdmin):
# list_display = ["descripcion", "imagen", "fecha", "comentario_publico", "album"]
# search_fields = ["descripcion", "comentario_publico"]
# ordering = ["descripcion"]
