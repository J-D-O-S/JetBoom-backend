from django.contrib.auth.views import LoginView
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = (
    [
        path(
            "iniciar_sesion/",
            LoginView.as_view(template_name="usuarios/iniciarSesion.html"),
            name="iniciar sesion",
        ),
    ]
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
)
