from django.urls import path 

from Materias.views import AsignaturaListView, AsignaturaDetail

urlpatterns = [
    path('', AsignaturaListView.as_view(), name='materias'),  #Todos
    path('<int:pk>/', AsignaturaDetail.as_view(), name='materia' )  #ID
]