from django.shortcuts import render
from rest_framework import viewsets
from .models import Ciudadano, Incidencia
from .serializers import CiudadanoSerializer, IncidenciaSerializer

# Create your views here.

class CiudadanoViewSet(viewsets.ModelViewSet):
    queryset = Ciudadano.objects.all()
    serializer_class = CiudadanoSerializer

class IncidenciaViewSet(viewsets.ModelViewSet):
    queryset = Incidencia.objects.all()
    serializer_class = IncidenciaSerializer