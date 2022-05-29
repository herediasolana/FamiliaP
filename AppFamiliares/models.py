from django.db import models

# Create your models here.

class Familiares(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    edad = models.IntegerField()
    nacimiento= models.DateField(blank=True, null=True)
    relacion = models.CharField(max_length=30)