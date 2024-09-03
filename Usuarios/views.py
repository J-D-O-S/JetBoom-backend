from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views import generic


class RegistroUsuario(generic.CreateView):
    form_class = UserCreationForm
    template_name = "usuarios/registrarse.html"
    success_url = reverse_lazy("iniciar sesion")


class IniciarSesion(LoginView):
    template_name = "usuarios/iniciarSesion.html"
