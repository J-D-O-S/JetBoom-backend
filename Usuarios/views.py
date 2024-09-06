from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.base import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import LoginForm, CustomUserCreationForm


# uso el View para poder hacer el get y post en la misma vista
class RegistroView(View):
    def get(self, request):
        form = CustomUserCreationForm()
        return render(request, "usuarios/crearCuenta.html", {"form": form})

    def post(self, request):
        form = CustomUserCreationForm(request.POST)
        # print(form.is_valid())
        # print(form.errors)
        if form.is_valid():
            form.save()
            return redirect("iniciar_sesion")  # TODO: Redirect to perfil page

        form = CustomUserCreationForm()
        return render(request, "usuarios/crearCuenta.html", {"form": form})


class LoginUsuarioView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, "usuarios/iniciarSesion.html", {"form": form})

    def post(self, request):
        form = LoginForm(request.POST)
        # print(form)
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]

            user = authenticate(request, username=email, password=password)

            if user is not None:
                login(request, user)
                return redirect("index")
            else:
                form.add_error(None, "Correo electrónico o contraseña incorrectos")
        return render(request, "usuarios/iniciarSesion.html", {"form": form})


class LogoutUsuarioView(View):
    def post(self, request):
        logout(request)
        return redirect("index")


class PerfilView(LoginRequiredMixin, TemplateView):
    template_name = "perfil/perfil.html"
