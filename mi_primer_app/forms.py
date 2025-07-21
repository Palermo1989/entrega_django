from django import forms
from .models import Paciente, Estudio , doctor

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = ['nombre', 'apellido', 'direccion', 'edad', 'obra_social']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'edad': forms.NumberInput(attrs={'class': 'form-control'}),
            'obra_social': forms.TextInput(attrs={'class': 'form-control'}),
        }

URGENCIA_CHOICES = [
    ('bajo', 'Bajo'),
    ('medio', 'Medio'),
    ('alta', 'Alta'),
]


class EstudioForm(forms.ModelForm):
    class Meta:
        model = Estudio
        fields = ['nombre', 'paciente', 'fecha', 'urgencia']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'paciente': forms.Select(attrs={'class': 'form-select'}),
            'fecha': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'urgencia': forms.Select(attrs={'class': 'form-select'}),
        }

class DoctorForm(forms.ModelForm):
    class Meta:
        model = doctor
        fields = ['nombre', 'apellido', 'edad', 'fecha_nacimiento', 'especialidad']
        widgets = {
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'edad': forms.NumberInput(attrs={'class': 'form-control'}),
            'especialidad': forms.TextInput(attrs={'class': 'form-control'}),
        }