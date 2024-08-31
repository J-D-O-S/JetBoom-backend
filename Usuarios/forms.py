from django import forms
from django.contrib.auth.forms import UserCreationForm
from Usuarios.models import Usuario, TipoIdentificacion


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Usuario
        fields = (
            "email",
            "nombre",
            "segundo_nombre",
            "apellido",
            "segundo_apellido",
            "numero_identificacion",
            "tipo_documento",
            "fecha_nacimiento",
            "password1",
            "password2",
        )

    tipo_documento = forms.ModelChoiceField(queryset=TipoIdentificacion.objects.all())
