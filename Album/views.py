# from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

from .models import AlbumFoto

from Usuarios.forms import CustomUserCreationForm


class AlbumFotosView(generic.TemplateView):
    template_name = "album.html"


class UserCreateView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("iniciar_sesion")
    template_name = "usuarios/crearCuenta.html"

    def form_valid(self, form):
        response = super(UserCreateView, self).form_valid(form)
        AlbumFoto.objects.create(usuario=self.object)
        return response
