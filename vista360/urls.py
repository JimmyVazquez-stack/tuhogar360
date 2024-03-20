from django.urls import path
from .views import Vista360

urlpatterns = [
    path('vista/', Vista360.as_view(), name='vista360'),
]