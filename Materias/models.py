from django.db import models

# Create your models here.
class Asignatura(models.Model):
    asignatura = models.CharField(max_length=100)
    duracion = models.IntegerField(null=True)
    horarios = models.CharField(max_length=30)
    disponibilidad = models.BooleanField(default=True)
    
    def __str__(self):
        return self.asignatura