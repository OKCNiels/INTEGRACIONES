from django.urls import path
from usuariomgc import views
#importmos las clases de los views para las rutas
urlpatterns_usuariomgc = [
    path('listar', views.listar, name='listar'),
    path('obtener/<str:email>', views.obtener, name='obtener'),
    # path('guardar-huella', views.guardarHuella, name='guardar-huella'),
]