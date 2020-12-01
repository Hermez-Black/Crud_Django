from django.db import models
from Materias.models import Asignatura
# Create your models here.
class Alumno(models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()
    grado = models.CharField(max_length=20)
    grupo = models.CharField(max_length=10)
    correo = models.CharField(max_length=200)
    calificacion = models.IntegerField(null=True)
    asistencia = models.IntegerField(null=True)

    clases = models.ManyToManyField(Asignatura, related_name='clases')

    def __str__(self):
        return self.nombre

        