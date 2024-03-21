from django.urls import path
from .views import UsuariosView, NosotrosView, AnunciosView, BlogView, ContactoView, RegistroUsuarioView, CustomLoginView, CustomLogoutView, PerfilUsuarioView

urlpatterns = [
    path('', UsuariosView.as_view(), name='usuarios'),
    path('nosotros/', NosotrosView.as_view(), name='nosotros'),
    path('anuncios/', AnunciosView.as_view(), name='anuncios'),
    path('blog/', BlogView.as_view(), name='blog'),
    path('contacto/', ContactoView.as_view(), name='contacto'),
    path('registro/', RegistroUsuarioView.as_view(), name='registro'),
    path('ingreso/', CustomLoginView.as_view(), name='ingreso'),
    path('logout/', CustomLogoutView.as_view(), name='logout' ),
    path('perfil/', PerfilUsuarioView.as_view(), name='perfil'),
]
