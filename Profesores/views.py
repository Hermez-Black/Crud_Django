from django.shortcuts import render
from rest_framework.views import APIView

from Profesores.models import Maestro
from Profesores.serializers import ProfeSerializer
# Create your views here.
# from django.views.generic import CreateView
from rest_framework import generics, status
from rest_framework.response import Response
# from .models import SampleObject
# from .forms import SampleObjectForm

# class CreateObject(CreateView):
#     model = SampleObject
#     form_class = SampleObjectForm
#     success_url = 'url_to_redirect_to'



# class ProfesorAPIView(APIView):

#     def get(self, request):
#         profesores = Maestro.objects.all()
#         serialized = ProfeSerializer(profesores, many=True)
#         return Response(status=status.HTTP_200_OK, data=serialized.data)

# Obtener y crear

class ProfesorListView(generics.ListCreateAPIView):
    queryset = Maestro.objects.all()
    serializer_class = ProfeSerializer

# Eliminar y Modificar 

class ProfeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Maestro.objects.all()
    serializer_class = ProfeSerializer