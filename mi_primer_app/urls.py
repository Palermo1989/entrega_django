from django.urls import path

from .views import (
    saludo, saludo_con_template, crear_doctor, inicio,
    crear_paciente, crear_estudio, buscar_paciente, lista_paciente
)

urlpatterns = [
    path('', inicio, name='inicio'),
    path('hola-mundo/', saludo),
    path('hola-mundo-template/', saludo_con_template),
    path('crear-doctor/', crear_doctor, name='crear-doctor'),
    path('crear-paciente/', crear_paciente, name='crear-paciente'),
    path('crear-estudio/', crear_estudio, name='crear-estudio'),
    path('pacientes/', lista_paciente, name='lista_paciente'),
    path('paciente/buscar/', buscar_paciente, name='buscar-paciente'),
]
