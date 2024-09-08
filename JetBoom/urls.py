"""
URL configuration for JetBoom project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include

from .views import IndexView
from Fidelizacion.views import AboutUsView
from django.conf.urls import handler404
from django.contrib.auth import views as auth_views
from .views import MyCustomPageNotFoundView

handler404 = MyCustomPageNotFoundView.as_view()

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("admin/", admin.site.urls),
    path("sobre_nosotros/", AboutUsView.as_view(), name="sobre_nosotros"),
    path("usuarios/", include("Usuarios.urls")),
    path("album/", include("Album.urls")),
    path("servicios/", include("Servicios.urls")),
    path("fidelizacion/", include("Fidelizacion.urls")),
    path(
        "recuperar_contrasenia/",
        auth_views.PasswordResetView.as_view(
            template_name="registrations/password_reset_form.html",
            email_template_name="registrations/password_reset_email.html",
        ),
        name="password_reset",
    ),
    path(
        "recuperar_contrasenia/completado/",
        auth_views.PasswordResetDoneView.as_view(
            template_name="registrations/password_reset_done.html",
        ),
        name="password_reset_done",
    ),
    path(
        "recuperar_contrasenia/confirmar/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(
            template_name="registrations/password_reset_confirm.html",
        ),
        name="password_reset_confirm",
    ),
    path(
        "recuperar_contrasenia/exitoso/",
        auth_views.PasswordResetCompleteView.as_view(
            template_name="registrations/password_reset_complete.html",
        ),
        name="password_reset_complete",
    ),
]
