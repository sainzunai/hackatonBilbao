from django.urls import path
from . import views


urlpatterns = [
   path('',views.index, name ='index'),
   path('busqueda/', views.Insertar.as_view(), name='insertar'),
   path('adivinar/', views.Adivinar.as_view(), name='adivinar'),
   path('graficos/', views.Pintar, name='pintar'),
  ]




