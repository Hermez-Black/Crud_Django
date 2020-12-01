from django.shortcuts import render
from rest_framework.views import APIView

from Estudiantes.models import Alumno
from Estudiantes.serializers import EstudianteSerializer
# Create your views here.
# from django.views.generic import CreateView
from rest_framework import generics, status
from rest_framework.response import Response
# Create your views here.

# Obtener y crear

class EstudiantesListView(generics.ListCreateAPIView):
    queryset = Alumno.objects.all()
    serializer_class = EstudianteSerializer

# Eliminar y Modificar 

class EstudiantesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Alumno.objects.all()
    serializer_class = EstudianteSerializer