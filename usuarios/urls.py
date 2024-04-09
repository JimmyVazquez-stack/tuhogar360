from django.urls import path
from .views import UsuariosView, NosotrosView, ContactoView, RegistroUsuarioView, CustomLoginView, CustomLogoutView, PerfilUsuarioView, PerfilUpdateView

urlpatterns = [
    path('', UsuariosView.as_view(), name='usuarios'),
    path('nosotros/', NosotrosView.as_view(), name='nosotros'),
    path('contacto/', ContactoView.as_view(), name='contacto'),
    path('registro/', RegistroUsuarioView.as_view(), name='registro'),
    path('ingreso/', CustomLoginView.as_view(), name='ingreso'),
    path('logout/', CustomLogoutView.as_view(), name='logout' ),
    path('perfil/', PerfilUsuarioView.as_view(), name='perfil'),
    path('perfil/editar/', PerfilUpdateView.as_view(), name='editar_perfil'),
]
