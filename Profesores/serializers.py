from rest_framework import serializers
from Profesores.models import Maestro

class ProfeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Maestro
        fields = ('__all__')