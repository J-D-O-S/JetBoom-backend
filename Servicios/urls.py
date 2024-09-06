from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import LugaresTuristicosView, DetalleLugarTuristicoView

urlpatterns = (
    [
        path(
            "lugares/",
            LugaresTuristicosView.as_view(),
            name="lugares_turisticos",
        ),
        path(
            "detalle_lugar/",
            DetalleLugarTuristicoView.as_view(),
            name="detalle_lugar",
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
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
)
