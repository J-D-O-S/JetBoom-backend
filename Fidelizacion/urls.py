from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import AboutUsView, ContactanosView

urlpatterns = (
    [
        path(
            "sobre_nosotros/",
            AboutUsView.as_view(),
            name="sobre_nosotros",
        ),
        path(
            "contactanos/",
            ContactanosView.as_view(),
            name="contactanos",
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
