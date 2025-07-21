from django.urls import path

from .views import (
    saludo, saludo_con_template, crear_doctor,modificar_doctor,eliminar_doctor, inicio,
    crear_paciente, crear_estudio, editar_estudio,eliminar_estudio,modificar_paciente,eliminar_paciente
)

urlpatterns = [
    path('', inicio, name='inicio'),
    path('hola-mundo/', saludo),
    path('hola-mundo-template/', saludo_con_template),
    path('crear-doctor/', crear_doctor, name='crear-doctor'),
    path('crear-paciente/', crear_paciente, name='crear-paciente'),
    path('crear-estudio/', crear_estudio, name='crear-estudio'),
    path('editar-estudio/<int:pk>/', editar_estudio, name='editar-estudio'),
    path('eliminar-estudio/<int:pk>/', eliminar_estudio, name='eliminar-estudio'),
    path('paciente/eliminar/<int:pk>/', eliminar_paciente, name='eliminar-paciente'),
    path('paciente/modificar/<int:pk>/', modificar_paciente, name='modificar-paciente'),
    path('modificar-doctor/<int:pk>/', modificar_doctor, name='modificar-doctor'),
    path('eliminar-doctor/<int:pk>/', eliminar_doctor, name='eliminar-doctor'),

]
