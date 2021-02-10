from django.shortcuts import render
from rest_framework.views import APIView
from Materias.models import Asignatura
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

def Index(request):
    return render(request, 'estudiante.html', {
        'Estudiantes': Alumno.objects.all(),
        'Mensaje': 'Este es un hola'
    })

def Index_id(request, id):
    estudiante = Alumno.objects.get(id=id)
    clases = estudiante.clases.all()  # ---> De ese estudiante de la variable de arriba tomamos las clases, NO DEL MODELO DE ALUMNO
    return render(request, 'estudiante_id.html', {
        'estudiante': estudiante,
        'clases': clases
    })