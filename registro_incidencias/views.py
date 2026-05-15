from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .models import Ciudadano, Incidencia
from .serializers import CiudadanoSerializer, IncidenciaSerializer

# Create your views here.

class CiudadanoViewSet(viewsets.ModelViewSet):
    queryset = Ciudadano.objects.all()
    serializer_class = CiudadanoSerializer

class IncidenciaViewSet(viewsets.ModelViewSet):
    queryset = Incidencia.objects.all()
    serializer_class = IncidenciaSerializer
    authentication_classes = []
    permission_classes = [AllowAny]

def ReportarIncidenciaView(request):
    return render(request, 'reportar_incidencia.html')