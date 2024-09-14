from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [
    path(
        "",
        auth_views.PasswordResetView.as_view(
            template_name="registrations/password_reset_form.html",
            email_template_name="registrations/password_reset_email.html",
        ),
        name="password_reset",
    ),
    path(
        "validando/",
        auth_views.PasswordResetDoneView.as_view(
            template_name="registrations/password_reset_done.html",
        ),
        name="password_reset_done",
    ),
    path(
        "confirmar/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(
            template_name="registrations/password_reset_confirm.html",
        ),
        name="password_reset_confirm",
    ),
    path(
        "exitoso/",
        auth_views.PasswordResetCompleteView.as_view(
            template_name="registrations/password_reset_complete.html",
        ),
        name="password_reset_complete",
    ),
]
