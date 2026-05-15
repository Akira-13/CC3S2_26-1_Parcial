from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.ReportarIncidenciaView, name='reportar_incidencia'),
]