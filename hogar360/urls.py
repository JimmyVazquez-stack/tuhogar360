from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('usuarios.urls')),
    path('administrativos/', include('administrativos.urls')),
    path('admin/', admin.site.urls),
    path('vista360/', include('vista360.urls')),
    path('catalogos/', include('catalogo.urls')),
    path('blog/', include('blog.urls')),
]
