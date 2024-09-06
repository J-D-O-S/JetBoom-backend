from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from Usuarios.models import Usuario

# from django.contrib.auth import get_user_model

# User = get_user_model()


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = Usuario
        fields = (
            "email",
            "nombre",
            "segundo_nombre",
            "apellido",
            "segundo_apellido",
            "numero_identificacion",
            "tipo_identificacion",
            "fecha_nacimiento",
        )


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = Usuario
        fields = (
            "email",
            "nombre",
            "segundo_nombre",
            "apellido",
            "segundo_apellido",
            "numero_identificacion",
            "tipo_identificacion",
            "fecha_nacimiento",
        )


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
