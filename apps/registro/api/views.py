from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from apps.registro.models import Registro
from apps.registro.api.serializers import RegistroSerializer


class RegistroApiView(APIView):
    def get(self,requets):
        serializer= RegistroSerializer(Registro.objects.all(), many = True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)
    
    def post(self,request):

        serializer =RegistroSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_200_OK, data=serializer.data)