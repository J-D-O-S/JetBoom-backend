from django.shortcuts import render
from django.views.generic.base import TemplateView

class SellView(TemplateView):
    template_name = "pago/pago.html"

class comprobanteView(TemplateView):
    template_name = "pago/comprobantePago.html"  

class pasarelaView(TemplateView):
    template_name = "pasarela_pago/pasarelaPago.html"      
    #  def get(self, request):
    #     return render(request, "pago.html")


    
