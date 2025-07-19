from django import forms
from .models import Paciente, Estudio

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
    ('baja', 'Baja'),
    ('media', 'Media'),
    ('alta', 'Alta'),
]

class EstudioForm(forms.ModelForm):
    urgencia = forms.ChoiceField(choices=URGENCIA_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Estudio
        fields = ['nombre', 'paciente', 'fecha', 'urgencia']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'paciente': forms.Select(attrs={'class': 'form-control'}),
            'fecha': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }