from django.contrib.auth.views import LoginView, LogoutView
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path

urlpatterns = (
    [
        path(
            "iniciar_sesion/",
            LoginView.as_view(),
            name="iniciar sesion",
        ),
        # path(
        #     "registrarse/",
        #     RegistroUsuario.as_view(),
        #     name="registrarse",
        # ),
        path(
            "cerrar_sesion/",
            LogoutView.as_view(),
            name="cerrar sesion",
        ),
    ]
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
)
