from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from datetime import date


class SellView(LoginRequiredMixin, TemplateView):
    template_name = "pago.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["fecha_min"] = date(1924, 1, 1)
        context["fecha_max"] = date(2006, 12, 31)
        return context

    def get(self, request):
        return render(request, "pago.html")

    def post(self, request):
        return render(request, "pago.html")
