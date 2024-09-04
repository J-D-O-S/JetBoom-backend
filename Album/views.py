from django.shortcuts import render
from django.views.generic import TemplateView


class LugaresTuristicosView(TemplateView):
    template_name = "lugaresTuristicos.html"
