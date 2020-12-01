from rest_framework import serializers
from Estudiantes.models import Alumno

class EstudianteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alumno
        fields = ('__all__')