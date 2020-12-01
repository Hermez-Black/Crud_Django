from django.urls import path 

from Estudiantes.views import EstudiantesListView, EstudiantesDetail

urlpatterns = [
    path('', EstudiantesListView.as_view(), name='estudiantes'),  #Todos
    path('<int:pk>/', EstudiantesDetail.as_view(), name='estudiante' )  #ID
]