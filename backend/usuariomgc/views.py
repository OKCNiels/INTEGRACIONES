from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
# lista de modelos
from usuariomgc.models import UsuariomgcModel
from usuariomgc.serializers import UsuariomgcSerializer

from django.http import JsonResponse
# Create your views here.

def listar(request):
    serializer = UsuariomgcSerializer(UsuariomgcModel.objects.all(), many=True)
    return JsonResponse([
        {
            "tipo":"success",
            "data":serializer.data
        }
    ], safe=False)
    # return Response(status=status.HTTP_200_OK, data=serializer.data)

def obtener(request,email):
    
    usuario = UsuariomgcSerializer(UsuariomgcModel.objects.filter(activo=True, deleted_at__isnull=True, email=email), many=True)

    return JsonResponse([
        {
            "tipo":"success",
            "data":usuario.data
        }
    ], safe=False)
    
# def guardarHuella(request):
#     if request.method == 'POST':
#         # Captura los datos enviados en la solicitud
#         data = request.POST  # Para datos form-urlencoded
#         # o usa request.body si los datos vienen en formato JSON
#         return JsonResponse({'mensaje': 'Datos recibidos', 'data': data})
#     else:
#         return JsonResponse({'error': 'Método no permitido'}, status=405)
    