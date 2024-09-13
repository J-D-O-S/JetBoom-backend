from django.shortcuts import render

from django.views.generic import TemplateView
from django.views.generic.base import View
from .forms import CustomFidelizacionForm


class AboutUsView(View):
    def get(self, request, *args, **kwargs):
        form = CustomFidelizacionForm()
        return render(request, "sobreNosotros/sobreNosotros.html", {"form": form})

    def post(self, request, *args, **kwargs):
        form = CustomFidelizacionForm(request.POST)
        print(form)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return render(request, "sobreNosotros/sobreNosotros.html")
        else:
            print("\n\nAquí se van a presentar los errores\n\n")
            print(form.errors)
            return render(request, "sobreNosotros/sobreNosotros.html")


class ContactanosView(TemplateView):
    template_name = "atencion_usuario/contactanos.html"
