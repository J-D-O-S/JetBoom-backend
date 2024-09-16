from django.shortcuts import render

from django.views.generic import TemplateView
from django.views.generic.base import View
from .forms import CustomFidelizacionForm

    
class AboutUsView(View):
    def get(self, request, *args, **kwargs):
        form = CustomFidelizacionForm()
        return render(request, "sobreNosotros/sobreNosotros.html", {"form": form})

    def post(self, request, *args, **kwargs):
        form = CustomFidelizacionForm(request.POST, request.FILES)
        print(form)
        if form.is_valid():
            user = self.request.user
            form.instance.usuario_id = user.id
            form.save()
            return render(request, "index.html", {"form": form})
        else:
            print("Errores en el formulario: ", form.errors)
            return render(request, "sobreNosotros/sobreNosotros.html", {"form": form})

class ContactanosView(TemplateView):
    template_name = "atencion_usuario/contactanos.html"

class terminosCondicionesView(TemplateView):
    template_name = "atencion_usuario/terminosCondiciones.html"    
