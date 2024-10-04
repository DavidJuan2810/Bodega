from rest_framework.viewsets import  ViewSet
from rest_framework.response import Response
from rest_framework import status
from apps.registro.models import Registro
from apps.registro.api.serializers import RegistroSerializer


class RegistroViewSet(ViewSet):
    def list(self,requets):
        serializer= RegistroSerializer(Registro.objects.all(), many = True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)
    
    def retrieve(self , requets, pk=int):
        serializer=RegistroSerializer(Registro.objects.get(pk=pk))
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    def update(self, request, pk=int):
        try:
            serializer = Registro.objects.get(pk=pk)
            serializer = RegistroSerializer(serializer, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        except Registro.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND, data= {"REGISTRO NO ENCONTRADO"})

    def partial_update(self, request, pk=int):
        try:
            serializer = Registro.objects.get(pk=pk)
            serializer = RegistroSerializer(serializer, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        except Registro.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND, data= {"REGISTRO NO ENCONTRADO"})
        
    def destroy(self, request, pk=int):
        serializer = Registro.objects.get(pk=pk)
        serializer.delete()
        return Response(status = status.HTTP_200_OK)

    def create(self,request):
        serializer =RegistroSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_200_OK, data=serializer.data)