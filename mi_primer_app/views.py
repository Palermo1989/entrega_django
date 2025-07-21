from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render
from .models import doctor, Paciente, Estudio
from .forms import DoctorForm, PacienteForm, EstudioForm
from django.contrib.auth import logout
from django.shortcuts import redirect


# Inicio y saludos
def inicio(request):
    return render(request, 'mi_primer_app/inicio.html')

def saludo(request):
    from django.http import HttpResponse
    return HttpResponse("¡Hola, mundo!")

def saludo_con_template(request):
    return render(request, 'mi_primer_app/saludo.html')


# ----------------------------
# DOCTOR
# ----------------------------

class DoctorCreateView(CreateView):
    model = doctor
    form_class = DoctorForm
    template_name = 'mi_primer_app/crear_doctor.html'
    success_url = reverse_lazy('crear-doctor')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['doctores'] = doctor.objects.all()
        return context

class DoctorUpdateView(UpdateView):
    model = doctor
    form_class = DoctorForm
    template_name = 'mi_primer_app/modificar_doctor.html'
    success_url = reverse_lazy('crear-doctor')

class DoctorDeleteView(DeleteView):
    model = doctor
    template_name = 'mi_primer_app/eliminar_doctor.html'
    success_url = reverse_lazy('crear-doctor')


# ----------------------------
# PACIENTE
# ----------------------------

class PacienteCreateView(CreateView):
    model = Paciente
    form_class = PacienteForm
    template_name = 'mi_primer_app/crear_paciente.html'
    success_url = reverse_lazy('crear-paciente')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pacientes'] = Paciente.objects.all()
        return context

class PacienteUpdateView(UpdateView):
    model = Paciente
    form_class = PacienteForm
    template_name = 'mi_primer_app/modificar_paciente.html'
    success_url = reverse_lazy('crear-paciente')

class PacienteDeleteView(DeleteView):
    model = Paciente
    template_name = 'mi_primer_app/eliminar_paciente.html'
    success_url = reverse_lazy('crear-paciente')


# ----------------------------
# ESTUDIO
# ----------------------------

class EstudioCreateView(CreateView):
    model = Estudio
    form_class = EstudioForm
    template_name = 'mi_primer_app/crear_estudio.html'
    success_url = reverse_lazy('crear-estudio')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['estudios'] = Estudio.objects.all().order_by('-fecha')
        return context

class EstudioUpdateView(UpdateView):
    model = Estudio
    form_class = EstudioForm
    template_name = 'mi_primer_app/modificar_estudio.html'
    success_url = reverse_lazy('crear-estudio')

class EstudioDeleteView(DeleteView):
    model = Estudio
    template_name = 'mi_primer_app/eliminar_estudio.html'
    success_url = reverse_lazy('crear-estudio')

    
def custom_logout(request):
    logout(request)
    return redirect('inicio')