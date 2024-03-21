from django.urls import path
from .views import DetallesCasaView
# Create your views here.
urlpatterns = [
    path('detalles/', DetallesCasaView.as_view(), name='detalles'),

]