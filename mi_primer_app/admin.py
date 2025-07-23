from django.contrib import admin
from .models import doctor, Paciente, Estudio


register_models = [doctor, Paciente, Estudio]
admin.site.register(register_models)
