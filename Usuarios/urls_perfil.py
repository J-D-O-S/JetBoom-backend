from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import (
    PerfilView,
    PuntosView,
    CustomUploadImageView,
)


urlpatterns = (
    [
        path(
            "",
            PerfilView.as_view(),
            name="perfil",
        ),
        path("puntos/", PuntosView.as_view(), name="puntos"),
        path("imagen_perfil/", CustomUploadImageView.as_view(), name="imagen_perfil"),
    ]
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
)
