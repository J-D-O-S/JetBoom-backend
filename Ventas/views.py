from django.shortcuts import render
from django.views.generic.base import TemplateView
from datetime import date


class SellView(TemplateView):
    template_name = "pago/pago.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["fecha_min"] = date(1924, 1, 1)
        context["fecha_max"] = date(2006, 12, 31)
        return context

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        return render(request, self.template_name)


class comprobanteView(TemplateView):
    template_name = "pago/comprobantePago.html"


class pasarelaView(TemplateView):
    template_name = "pasarela_pago/pasarelaPago.html"
