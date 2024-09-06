from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import Usuario


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = Usuario
    list_display = ["email", "nombre", "apellido", "is_staff", "is_active"]
    list_filter = ["is_staff", "is_active", "is_superuser"]
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (
            "Información Personal",
            {
                "fields": (
                    "nombre",
                    "segundo_nombre",
                    "apellido",
                    "segundo_apellido",
                    "fecha_nacimiento",
                    "numero_identificacion",
                    "tipo_identificacion",
                )
            },
        ),
        ("Permisos", {"fields": ("is_staff", "is_active", "is_superuser")}),
        ("Fechas Importantes", {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "nombre",
                    "apellido",
                    "password1",
                    "password2",
                    "is_staff",
                    "is_active",
                    "is_superuser",
                ),
            },
        ),
    )
    search_fields = ("email",)
    ordering = ("email",)


admin.site.register(Usuario, CustomUserAdmin)
