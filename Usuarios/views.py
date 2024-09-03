from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from .forms import CustomUserCreationForm


class RegistroView(CreateView):
    form_class = CustomUserCreationForm
    template_name = "usuarios/crearCuenta.html"
    success_url = reverse_lazy("iniciar sesion")  # TODO: change this to the correct URL

    def form_valid(self, form):
        response = super().form_valid(form)
        return response


class LoginUsuarioView(LoginView):
    template_name = "usuarios/iniciarSesion.html"


class LogoutUsuarioView(LogoutView):
    next_page = "iniciar sesion"
