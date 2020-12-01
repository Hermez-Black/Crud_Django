from django.db import models
from Materias.models import Asignatura
# Create your models here.
class Maestro(models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()
    profesion = models.CharField(max_length=100)

    clases_impartidas = models.ManyToManyField(Asignatura, related_name='clases_impartidas')

    def __str__(self):
        return self.nombre