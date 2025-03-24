from django.urls import path
from usuariomgc import views
#importmos las clases de los views para las rutas
from usuariomgc.views import HuellaApiView
urlpatterns_usuariomgc = [
    path('listar', views.listar, name='listar'),
    path('obtener/<str:email>', views.obtener, name='obtener'),
    # path('guardar-huella', views.guardarHuella, name='guardar-huella'),
    path('guardar-huella', HuellaApiView.as_view(), name='guardar-huella'),
]