from django import forms
from .models import Paciente, Estudio

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = ['nombre', 'apellido', 'direccion', 'edad', 'obra_social']

class EstudioForm(forms.ModelForm):
    class Meta:
        model = Estudio
        fields = ['nombre', 'paciente', 'fecha', 'urgencia']