from django.urls import path
from .views import UsuariosView, NosotrosView, AnunciosView, BlogView, ContactoView, RegistroView

urlpatterns = [
    path('', UsuariosView.as_view(), name='usuarios'),
    path('nosotros/', NosotrosView.as_view(), name='nosotros'),
    path('anuncios/', AnunciosView.as_view(), name='anuncios'),
    path('blog/', BlogView.as_view(), name='blog'),
    path('contacto/', ContactoView.as_view(), name='contacto'),
    path('registro/', RegistroView.as_view(), name='registro'),
]
