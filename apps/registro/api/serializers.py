from rest_framework.serializers import ModelSerializer
from apps.registro.models import Registro

class RegistroSerializer(ModelSerializer):
    class Meta:
        model=Registro
        fields = ['nombre','categoria','cantidad','fechaIngreso',]