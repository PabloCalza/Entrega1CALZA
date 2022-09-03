from django.urls import path
from AppCalza.views import *

urlpatterns = [
    path('', inicio, name='inicio'),
    path('medicos/', medicos, name='medicos'),
    path('enfermeras/', enfermeras, name="enfermeras"),
    path('pacientes/', pacientes, name="pacientes"),
    path('busquedaMatricula/', busquedaMatricula, name="busquedaMatricula"),
    path("buscar/", buscar, name="buscar"),

]