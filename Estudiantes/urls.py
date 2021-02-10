from django.urls import path 
from Estudiantes.views import Index, Index_id
from Estudiantes.views import EstudiantesListView, EstudiantesDetail
from Estudiantes.models import Alumno

urlpatterns = [
    # path('', EstudiantesListView.as_view(), name='estudiantes'),  #Todos
    path('', Index),
    # path('<int:pk>/', EstudiantesDetail.as_view(), name='estudiante' ),  #ID
    path('<id>/', Index_id)
]