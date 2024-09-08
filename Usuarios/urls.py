from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import (
    LoginUsuarioView,
    LogoutUsuarioView,
    RegistroView,
    PerfilView,
    PuntosView,
    CustomResetPasswordView,
)

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
        path(
            "perfil/",
            PerfilView.as_view(),
            name="perfil",
        ),
        path("perfil_puntos/", PuntosView.as_view(), name="puntos"),
        # path(
        #     "recuperar_contrasena/",
        #     CustomResetPasswordView.as_view(),
        #     name="reset_password",
        # ),
    ]
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
)
