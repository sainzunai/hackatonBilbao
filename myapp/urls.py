from django.urls import path
from . import views
from . import views


urlpatterns = [
   path('',views.index, name ='index'),
   path('busqueda/', views.Insertar.as_view(), name='insertar'),
  ]




