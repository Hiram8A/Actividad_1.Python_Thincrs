from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index' ),
    path('home/', views.Inicio.as_view(), name= 'home' ),
    path('insertar/', views.insertar_producto, name='insertar' ),
] 