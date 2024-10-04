#1 metodo#from rest_framework.views import APIView
#2 metodo#from rest_framework.viewsets import ViewSet
from rest_framework.viewsets import ModelViewSet
#from rest_framework.response import Response
#from rest_framework import status
from apps.registro.models import Registro
from apps.registro.api.serializers import RegistroSerializer

class RegistroModelViewSet(ModelViewSet):
    serializer_class = RegistroSerializer
    queryset = Registro.objects.all()

    #1 forma def get(self,request):
    #2def list(self,request):
    #2
    #2    serializer = RegistroSerializer(Registro.objects.all(), many=True)
    #2    return Response(status=status.HTTP_200_OK, data=serializer.data)
    #2
    #2def retrieve(self,request,pk=int):
    #2    try:
    #2        serializer = RegistroSerializer(Registro.objects.get(pk=pk))
    #2        return Response(status=status.HTTP_200_OK, data=serializer.data)
    #2    except Registro.DoesNotExist:
    #2        return Response(status=status.HTTP_400_BAD_REQUEST,data=("dato no encotrado"))
    #2    
    #1 forma def post(self,request):
    #2def create(self,request):
    #2    try:
    #2        serializer = RegistroSerializer(data=request.data)
    #2        serializer.is_valid(raise_exception=True)
    #2        serializer.save()
    #2        return Response(status=status.HTTP_200_OK, data=serializer.data)
    #2    except:
    #2        return Response(status=status.HTTP_404_NOT_FOUND,data=("error al crear nuevos datos"))
    #2
    #2def update(self,request,pk):
    #2    try:
    #2        serializer = Registro.objects.get(pk=pk)
    #2        serializer = RegistroSerializer(serializer,data=request.data)
    #2        serializer.is_valid(raise_exception=True)
    #2        serializer.save()
    #2        return Response(status=status.HTTP_200_OK,data=serializer.data)
    #2    except Registro.DoesNotExist:
    #2        return Response(status=status.HTTP_404_NOT_FOUND,data=("salida no encontrada."))
    #2    
    #2def partial_update(self,request,pk):
    #2    try:
    #2        serializer = Registro.objects.get(pk=pk)
    #2        serializer = RegistroSerializer(serializer,data=request.data, partial=True)
    #2        serializer.is_valid(raise_exception=True)
    #2        serializer.save()
    #2        return Response(status=status.HTTP_200_OK,data=serializer.data)
    #2    except Registro.DoesNotExist:
    #2        return Response(status=status.HTTP_404_NOT_FOUND,data=("salida no encontrada."))
    #2    
    #2def destroy(self,request,pk):
    #2        serializer = Registro.objects.get(pk=pk)
    #2        serializer.delete()
    #2        return Response(status=status.HTTP_200_OK)