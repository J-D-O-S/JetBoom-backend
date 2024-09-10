from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import (
    PerfilView,
    PuntosView,
    CustomUploadImageView,
    ReservasView,
    ComprasView,
)


urlpatterns = (
    [
        path(
            "",
            PerfilView.as_view(),
            name="perfil",
        ),
        path("puntos/", PuntosView.as_view(), name="puntos"),
        path("reservas/", ReservasView.as_view(), name="reservas"),
        path("compras/", ComprasView.as_view(), name="compras"),
        path("imagen_perfil/", CustomUploadImageView.as_view(), name="imagen_perfil"),
        path("imagen_portada/", CustomUploadImageView.as_view(), name="imagen_portada"),
        path("imagen_galeria/", CustomUploadImageView.as_view(), name="imagen_galeria"),
    ]
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
)
