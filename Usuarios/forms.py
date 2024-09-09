from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Usuario

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


class ImagenUploadForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ["foto_perfil"]


# class CustomResetPasswordForm(forms.Form):
#     email = forms.EmailField()

#     def clean_email(self):
#         email = self.cleaned_data.get("email")
#         if not Usuario.objects.filter(email=email).exists():
#             raise forms.ValidationError("No existe un usuario con ese correo electrónico")
#         return email

#     def save(self):
#         email = self.cleaned_data.get("email")
#         user = Usuario.objects.get(email=email)
#         user.send_reset_password_email()
#         return user
