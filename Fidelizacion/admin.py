from django.contrib import admin
from .models import FidelizacionModel, Reto


# Registrar el modelo FidelizacionModel
@admin.register(FidelizacionModel)
class FidelizacionModelAdmin(admin.ModelAdmin):
    list_display = ("opinion_servicio", "tipo_solicitud", "usuario", "archivo_adjunto")
    list_filter = ("tipo_solicitud", "usuario")
    search_fields = ("opinion_servicio", "usuario__username")


# Registrar el modelo Reto
@admin.register(Reto)
class RetoAdmin(admin.ModelAdmin):
    list_display = (
        "nombre",
        "fecha_inicio",
        "fecha_fin",
        "punto_por_ganar",
        "is_active",
        "reto_completado",
    )
    list_filter = ("is_active", "reto_completado", "fecha_inicio", "fecha_fin")
    search_fields = ("nombre", "descripcion")
