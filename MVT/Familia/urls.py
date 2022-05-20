from django.urls import path
from Familia import views


urlpatterns = [
    path('', views.Mostrar, name="Mostrar"),
    path('agregar/', views.Agregar, name="agregar"),
    path('Borrar/<identificador>', views.Borrar, name="Borrar")
]