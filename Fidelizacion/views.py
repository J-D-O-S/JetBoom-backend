from django.shortcuts import render

# from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


class AboutUsView(TemplateView):
    template_name = "sobreNosotros/sobreNosotros.html"
