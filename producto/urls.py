from django.urls import path
from . import views

urlpatterns = [
    path('producto', views.producto, name='producto'),
    path('marca', views.marca, name='marca'),
    
]