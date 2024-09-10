from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.views.generic.base import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import LoginForm, CustomUserCreationForm, ImagenUploadForm
from Album.forms import ImagenUploadForm as AlbumImagenUploadForm, CustomFotoForm
from Album.models import AlbumFoto, Foto


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

    def get(self, request):
        album = AlbumFoto.objects.get(usuario=request.user)
        fotos = album.foto_set.all()
        return render(request, "perfil/perfil.html", {"album": album, "imagenes": fotos})


class PuntosView(LoginRequiredMixin, TemplateView):
    template_name = "perfil/perfilPuntos.html"


class ReservasView(LoginRequiredMixin, TemplateView):
    # hacer query para saber si hay reservas y renderizar la vista correspondiente
    # con la información de las reservas
    # template_name = "perfil/perfilReservasContenido.html"
    # sin la información de las reservas
    template_name = "perfil/perfilReservasSinContenido.html"


class ComprasView(LoginRequiredMixin, TemplateView):
    # hacer query para saber si hay compras y renderizar la vista correspondiente
    # con la información de las compras
    # template_name = "perfil/perfilCompras.html"
    # sin la información de las compras
    template_name = "perfil/perfilSinCompras.html"


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

        print(form_type)
        if form_type == "perfil":
            form = ImagenUploadForm(request.POST, request.FILES)
            self._save_image(request.user, form, "foto_perfil")
        elif form_type == "portada":
            form = AlbumImagenUploadForm(request.POST, request.FILES)
            user_album = request.user.albumfoto
            self._save_image(user_album, form, "foto_portada")
        elif form_type == "galeria":
            form = CustomFotoForm(request.POST, request.FILES)
            
            self._save_image_to_album(request.user, form)
        return redirect("perfil")

    def _save_image(self, user, form, field_name):
        if form.is_valid():
            setattr(user, field_name, form.cleaned_data[field_name])
            user.save()
            return redirect("perfil")
        else:
            print(form.errors)
            return render(self.request, "perfil/perfil.html", {"form": form})
    
    def _save_image_to_album(self, user, form):
        if form.is_valid():
            album = user.albumfoto
            
            image = form.cleaned_data["imagen"]
            img = Foto.objects.create(album = album, imagen=image)
            # img = form.save(commit=False)
            # img.album = album
            img.save()
            return redirect("perfil")
        else:
            print(form.errors)
            return render(self.request, "perfil/perfil.html", {"form": form})
