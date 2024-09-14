from django import forms
from .models import FidelizacionModel


class CustomFidelizacionForm(forms.ModelForm):
    class Meta:
        model = FidelizacionModel
        fields = (
            "opinion_servicio",
            "tipo_solicitud",
            "archivo_adjunto",
        )