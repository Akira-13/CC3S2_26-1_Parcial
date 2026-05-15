from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import IncidenciaViewSet, CiudadanoViewSet

router = DefaultRouter()
router.register(r'incidencias', IncidenciaViewSet)
router.register(r'ciudadanos', CiudadanoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]