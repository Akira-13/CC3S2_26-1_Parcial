from django.contrib import admin

# Register your models here.
from .models import Ciudadano, Incidencia

admin.site.register(Ciudadano)
admin.site.register(Incidencia)