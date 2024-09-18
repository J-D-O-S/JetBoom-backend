from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class SellView(LoginRequiredMixin, TemplateView):
    template_name = "pago.html"

    def get(self, request):
        return render(request, "pago.html")

    def post(self, request):
        return render(request, "pago.html")
