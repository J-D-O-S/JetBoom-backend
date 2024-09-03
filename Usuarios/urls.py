from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import LoginUsuarioView, LogoutUsuarioView, RegistroView

urlpatterns = (
    [
        path(
            "iniciar_sesion/",
            LoginUsuarioView.as_view(),
            name="iniciar_sesion",
        ),
        path(
            "registrarse/",
            RegistroView.as_view(),
            name="registrarse",
        ),
        path(
            "cerrar_sesion/",
            LogoutUsuarioView.as_view(),
            name="cerrar_sesion",
        ),
    ]
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
)
