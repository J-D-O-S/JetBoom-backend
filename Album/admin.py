from django.contrib import admin


# para el album de fotos
class CustomAlbumAdmin(admin.ModelAdmin):
    list_display = ["nombre", "descripcion", "fecha_creacion", "fecha_modificacion"]
    search_fields = ["nombre", "descripcion"]
    ordering = ["nombre"]
