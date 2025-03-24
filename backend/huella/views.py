from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated ## importacion de autenticacion por JWT
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
# lista de modelos
from huella.models import HuellaModel
from huella.serializers import HuellaSerializer

#llamamos la libreria para el huellero biometrico
from pyzkfp import ZKFP2

class HuellaApiView(APIView):
    # permission_classes = [IsAuthenticated] # oliga al usuario a envair el token por el api para el consumo de las rutas
    def post(self, request):
        dedo_id = request.data.get('dedo_id')
        usuario_id = request.data.get('usuario_id')
        
        # Inicializar la clase ZKFP2 y abrir el dispositivo
        zkfp2 = ZKFP2()
        zkfp2.Init()
    
        # Obtener el número de dispositivos y abrir el primero
        device_count = zkfp2.GetDeviceCount()
        # print(f"{device_count} dispositivos encontrados, conectando al primero.")
        zkfp2.OpenDevice(0)
    
        # Capturar una huella dactilar
        # print(f"Ingrese la primera huella")
        while True:
            capture = zkfp2.AcquireFingerprint()
            if capture:
                break

        # Realizar una comparación 1:N
        tmp, img = capture # descompone la huella en tmp que es la plantilla y img que es la imagen 
        finger_id, score = zkfp2.DBIdentify(tmp)
       
        # Apagar el dispositivo y liberar recursos
        zkfp2.CloseDevice()
        # zkfp2.Finalize()
        zkfp2.Terminate()
             
        
        img.imagen.save("huella.png", ContentFile(img), save=False)
        serializer = HuellaSerializer(HuellaModel.objects.create(
            usuario_id=request.data.get('usuario_id'),
            dedo_id=request.data.get('dedo_id'),
            plantila=tmp,
            imagen=img,
            estado=1,
        ))
        return Response(status=status.HTTP_200_OK, data= 's')