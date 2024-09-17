from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import AlbumFotosView

urlpatterns = [
    path(
        "album_fotos/",
        AlbumFotosView.as_view(),
        name="album",
    ),
    # path(
    #     "cerrar_sesion/",
    #     LogoutUsuarioView.as_view(),
    #     name="cerrar_sesion",
    # ),
    # path(
    #     "perfil/",
    #     PerfilView.as_view(),
    #     name="perfil",
    # ),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
