from django.db import models

# Create your models here.

class Ciudadano(models.Model):
    dni = models.CharField(max_length=8, unique=True, primary_key=True)
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=20)

class Incidencia(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(max_length=1000)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    evidencia = models.FileField(upload_to='evidencias/', null=True, blank=True)
    estado = models.CharField(max_length=50, default='Abierta')
    ciudadano = models.ForeignKey(Ciudadano, on_delete=models.CASCADE)