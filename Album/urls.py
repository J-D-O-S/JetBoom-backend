from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import LugaresTuristicosView

urlpatterns = (
    [
        path(
            "lugares_turisticos/",
            LugaresTuristicosView.as_view(),
            name="lugares_turisticos",
        ),
        # path(
        #     "registrarse/",
        #     RegistroView.as_view(),
        #     name="registrarse",
        # ),
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
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
)
