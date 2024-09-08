from django.shortcuts import render
from django.views.generic import TemplateView


class LugaresTuristicosView(TemplateView):
    template_name = "lugares/lugaresTuristicos.html"


class DetalleLugarTuristicoView(TemplateView):
    template_name = "lugares/lugarTuristico.html"
