from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import SellView

urlpatterns = (
    [
        path("", SellView.as_view(), name="pago"),
    ]
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
)