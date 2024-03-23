from django.db import models
from .models import *

# Create your models here.
class Equipo(models.Model):
    nombre = models.CharField(max_length=60)
    
    class Meta:
       ordering = ["nombre"]
    
    def __str__(self):
        return f"{self.nombre}"

class Posicion(models.Model):
    nombre = models.CharField(max_length=60)
    
    class Meta:
        verbose_name = "Posicion"
        verbose_name_plural = "Posiciones"
    
    def __str__(self):
        return f"{self.nombre}"

class Goleador(models.Model):
    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=60)
    
    class Meta:
        verbose_name = "Goleador"
        verbose_name_plural = "Goleadores"
    
    def __str__(self):
        return f"{self.nombre}, {self.apellido}"
    


    
    