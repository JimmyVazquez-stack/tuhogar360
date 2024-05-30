from django.urls import path
from .views import DetallesCasaView, AnunciosView, Vista360View, MisPublicacionesView, NuevaPublicacion, consulta_sepomex, DetallesCasaTodosView
# Create your views here.
urlpatterns = [
    path('anuncios/', AnunciosView.as_view(), name='anuncios'),
    path('detalles/<int:propiedad_id>/', DetallesCasaView.as_view(), name='detalles'),
    path('vista360/', Vista360View.as_view(), name='vista360'),
    path('mis_publicaciones/<str:username>/', MisPublicacionesView.as_view(), name='mis_publicaciones'),
    path('nueva_publicacion/', NuevaPublicacion.as_view(), name='nueva_publicacion'),
    path('consulta_sepomex/', consulta_sepomex, name='consulta_sepomex'),
    path('detalles_todos/<int:propiedad_id>/', DetallesCasaTodosView.as_view(), name='detalles_todos'),
]