# formulario para admin para poder hacer la creación del album de fotos
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Album, Foto
from django.contrib.auth import get_user_model

User = get_user_model()


class CustomAlbumForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = Album
        fields = (
            "usuario",
            "nombre_album",
            "descripcion",
        )
