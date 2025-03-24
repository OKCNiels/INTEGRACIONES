from django.urls import path
from usuariomgc import views
#importmos las clases de los views para las rutas
from huella.views import HuellaApiView
from huella.views import CompararApiView
urlpatterns_huella = [
    path('guardar', HuellaApiView.as_view()),
    path('comparar', CompararApiView.as_view()),
]