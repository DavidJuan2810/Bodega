from rest_framework.serializers import ModelSerializer
from apps.salida.models import Salida


class SalidaSerializer(ModelSerializer):
    class Meta:
        model = Salida
        fields = '__all__'
        #fields={'nombre','categoria','cantidad','FechaSalida'}