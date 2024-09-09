from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.views.generic.base import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import LoginForm, CustomUserCreationForm, ImagenUploadForm
from Album.models import AlbumFoto


# uso el View para poder hacer el get y post en la misma vista
class RegistroView(View):
    def get(self, request):
        form = CustomUserCreationForm()
        return render(request, "usuarios/crearCuenta.html", {"form": form})

    def post(self, request):
        form = CustomUserCreationForm(request.POST)
        print("\n impresión del formulario")
        print(form)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password1"])

            user.save()
            AlbumFoto.objects.create(usuario=user)

            username = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=password)
            if user is not None:
                print("\n\nUsuario autenticado\n\n")
                login(request, user)
                return redirect("perfil")
        else:
            print(form.errors)

        form = CustomUserCreationForm()
        return render(request, "usuarios/crearCuenta.html", {"form": form})


class LoginUsuarioView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, "usuarios/iniciarSesion.html", {"form": form})

    def post(self, request):
        form = LoginForm(request.POST)
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


class PuntosView(LoginRequiredMixin, TemplateView):
    template_name = "perfil/perfilPuntos.htm"


class CustomResetPasswordView(TemplateView, View):
    template_name = "registrations/password_reset_form.html"

    def post(self, request):
        pass


class CustomUploadImageView(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        form = ImagenUploadForm()
        return render(request, "perfil/perfil.html", {"form": form})

    def post(self, request):
        form_type = request.POST.get("form_type")

        if form_type == "perfil":
            form = ImagenUploadForm(request.POST, request.FILES)
            self._save_image(request.user, form)
        elif form_type == "portada":
            self._save_image(request.user, ImagenUploadForm)
        return redirect("perfil")

    def _save_image(self, user, form):
        if form.is_valid():
            user.foto_perfil = form.cleaned_data["foto_perfil"]
            user.save()

            return redirect("perfil")
        else:
            print(form.errors)
            return render(self.request, "perfil/perfil.html", {"form": form})
