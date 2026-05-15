from django.db import models

# Create your models here.

class Ciudadano(models.Model):
    dni = models.CharField(max_length=8, unique=True, primary_key=True)
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=20)

class Incidencia(models.Model):
    ESTADO_PENDIENTE = 'PENDIENTE'
    ESTADO_EN_REVISION = 'EN REVISION'
    ESTADO_REVISADO = 'REVISADO'

    ESTADO_CHOICES = [
        (ESTADO_PENDIENTE, 'Pendiente'),
        (ESTADO_EN_REVISION, 'En revision'),
        (ESTADO_REVISADO, 'Revisado'),
    ]

    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(max_length=1000)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    evidencia = models.FileField(upload_to='evidencias/', null=True, blank=True)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default=ESTADO_PENDIENTE)
    ciudadano = models.ForeignKey(Ciudadano, on_delete=models.CASCADE)