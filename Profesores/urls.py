from django.urls import path 

from Profesores.views import ProfesorListView, ProfeDetail

urlpatterns = [
    path('', ProfesorListView.as_view(), name='profesores'),
    path('<int:pk>/', ProfeDetail.as_view(), name='profe' )
]