from django.shortcuts import render
from rest_framework.views import APIView

from Materias.models import Asignatura
from Materias.serializers import AsignaturaSerializer
# Create your views here.
# from django.views.generic import CreateView
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework import viewsets
# from rest_framework.permissions import (
#     AllowAny,
#     IsAuthenticated
# )
# Create your views here.
# Obtener y crear

# crud
class AsignaturaViewSet(viewsets.ModelViewSet):
    queryset = Asignatura.objects.all()
    serializer_class = AsignaturaSerializer
    # permission_classes = (IsAuthenticated)


# class AsignaturaListView(generics.ListCreateAPIView):
#     queryset = Asignatura.objects.all()
#     serializer_class = AsignaturaSerializer

# # Eliminar y Modificar 

# class AsignaturaDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Asignatura.objects.all()
#     serializer_class = AsignaturaSerializer