from django.urls import path 

# from Materias.views import AsignaturaListView, AsignaturaDetail

from rest_framework.routers import DefaultRouter
from Materias.views import AsignaturaViewSet
router = DefaultRouter()

router.register(r'', AsignaturaViewSet)
urlpatterns = router.urls

# urlpatterns = [
#     path('', AsignaturaListView.as_view(), name='materias'),  #Todos
#     path('<int:pk>/', AsignaturaDetail.as_view(), name='materia' )  #ID
# ]