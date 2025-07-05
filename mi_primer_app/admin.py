from django.contrib import admin

# Register your models here.
from .models import doctor, paciente, Estudio

register_models = [doctor, paciente, Estudio]

admin.site.register(register_models)
