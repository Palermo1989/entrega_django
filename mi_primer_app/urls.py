from django.urls import path
from .views import (
    inicio, saludo, saludo_con_template, custom_logout,
    DoctorCreateView, DoctorUpdateView, DoctorDeleteView,
    PacienteCreateView, PacienteUpdateView, PacienteDeleteView,
    EstudioCreateView, EstudioUpdateView, EstudioDeleteView
)

urlpatterns = [
    path('', inicio, name='inicio'),
    path('hola-mundo/', saludo),
    path('hola-mundo-template/', saludo_con_template),

    # Logout personalizado
    path('logout/', custom_logout, name='logout'),

    # Doctor
    path('crear-doctor/', DoctorCreateView.as_view(), name='crear-doctor'),
    path('modificar-doctor/<int:pk>/', DoctorUpdateView.as_view(), name='modificar-doctor'),
    path('eliminar-doctor/<int:pk>/', DoctorDeleteView.as_view(), name='eliminar-doctor'),

    # Paciente
    path('crear-paciente/', PacienteCreateView.as_view(), name='crear-paciente'),
    path('modificar-paciente/<int:pk>/', PacienteUpdateView.as_view(), name='modificar-paciente'),
    path('eliminar-paciente/<int:pk>/', PacienteDeleteView.as_view(), name='eliminar-paciente'),

    # Estudio
    path('crear-estudio/', EstudioCreateView.as_view(), name='crear-estudio'),
    path('modificar-estudio/<int:pk>/', EstudioUpdateView.as_view(), name='modificar-estudio'),
    path('eliminar-estudio/<int:pk>/', EstudioDeleteView.as_view(), name='eliminar-estudio'),
]
