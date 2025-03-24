from django.urls import path
from usuariomgc import views
#importmos las clases de los views para las rutas
from huella.views import HuellaApiView
urlpatterns_huella = [
    path('guardar', HuellaApiView.as_view(), name='guardar-huella'),
]