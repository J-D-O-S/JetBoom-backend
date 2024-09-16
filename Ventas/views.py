from django.shortcuts import render
from django.views.generic.base import TemplateView

class SellView(TemplateView):
    template_name = "pago/pago.html"
    #  def get(self, request):
    #     return render(request, "pago.html")
