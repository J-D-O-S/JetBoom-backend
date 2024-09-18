from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import SellView, comprobanteView, pasarelaView

urlpatterns = (
    [
        path("", 
             SellView.as_view(), 
             name="pago"),
        path("comprobante_pago/", comprobanteView.as_view(), 
             name="comprobante_pago"),
        path("pasarela_pago/", 
             pasarelaView.as_view(), 
             name="pasarela_pago"),

    
    ]
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
)