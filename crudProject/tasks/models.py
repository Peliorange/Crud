from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Tasks(models.Model):
    titulo= models.CharField(max_length=50)
    descripcion= models.TextField(blank=True)
    proyecto= models.CharField(max_length=200)
    espacio= models.CharField(max_length=200)
    creador = models.ForeignKey(User, on_delete=models.CASCADE)
    tareaPadre= models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, related_name="subtareas")
    prioridad= models.CharField(max_length=10, default='media')
    fechaInicio= models.DateField()
    fechaVencimiento= models.DateField()

def __str__(self):
    return self.titulo
