# formulario para admin para poder hacer la creación del album de fotos
from django import forms
from .models import AlbumFoto, Foto

# from django.contrib.auth import get_user_model

# User = get_user_model()


class CustomAlbumForm(forms.ModelForm):
    class Meta(forms.ModelForm):
        model = AlbumFoto
        fields = (
            "usuario",
            "nombre_album",
            "descripcion",
        )


class CustomFotoForm(forms.ModelForm):
    class Meta(forms.ModelForm):
        model = Foto
        fields = (
            "album",
            "descripcion",
            "imagen",
            "comentario_publico",
        )
