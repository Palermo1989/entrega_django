from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from .models import doctor, Paciente, Estudio
from .forms import DoctorForm, PacienteForm, EstudioForm
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# ----------------------------
# INICIO Y SALUDOS
# ----------------------------

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

class DoctorCreateView(LoginRequiredMixin, CreateView):
    model = doctor
    form_class = DoctorForm
    template_name = 'mi_primer_app/crear_doctor.html'
    success_url = reverse_lazy('crear-doctor')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['doctores'] = doctor.objects.all()
        return context

class DoctorUpdateView(LoginRequiredMixin, UpdateView):
    model = doctor
    form_class = DoctorForm
    template_name = 'mi_primer_app/modificar_doctor.html'
    success_url = reverse_lazy('crear-doctor')

class DoctorDeleteView(LoginRequiredMixin, DeleteView):
    model = doctor
    template_name = 'mi_primer_app/eliminar_doctor.html'
    success_url = reverse_lazy('crear-doctor')


# ----------------------------
# PACIENTE
# ----------------------------

class PacienteCreateView(LoginRequiredMixin, CreateView):
    model = Paciente
    form_class = PacienteForm
    template_name = 'mi_primer_app/crear_paciente.html'
    success_url = reverse_lazy('crear-paciente')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pacientes'] = Paciente.objects.all()
        return context

class PacienteUpdateView(LoginRequiredMixin, UpdateView):
    model = Paciente
    form_class = PacienteForm
    template_name = 'mi_primer_app/modificar_paciente.html'
    success_url = reverse_lazy('crear-paciente')

class PacienteDeleteView(LoginRequiredMixin, DeleteView):
    model = Paciente
    template_name = 'mi_primer_app/eliminar_paciente.html'
    success_url = reverse_lazy('crear-paciente')


# ----------------------------
# ESTUDIO
# ----------------------------

class EstudioCreateView(LoginRequiredMixin, CreateView):
    model = Estudio
    form_class = EstudioForm
    template_name = 'mi_primer_app/crear_estudio.html'
    success_url = reverse_lazy('crear-estudio')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['estudios'] = Estudio.objects.all().order_by('-fecha')
        return context

class EstudioUpdateView(LoginRequiredMixin, UpdateView):
    model = Estudio
    form_class = EstudioForm
    template_name = 'mi_primer_app/modificar_estudio.html'
    success_url = reverse_lazy('crear-estudio')

class EstudioDeleteView(LoginRequiredMixin, DeleteView):
    model = Estudio
    template_name = 'mi_primer_app/eliminar_estudio.html'
    success_url = reverse_lazy('crear-estudio')


# ----------------------------
# FUNCIONES ADICIONALES
# ----------------------------

@login_required
def custom_logout(request):
    logout(request)
    return redirect('inicio')

def about(request):
    return render(request, 'about.html')

# Esta vista ahora es pública
def lista_doctores(request):
    doctores = doctor.objects.all()
    return render(request, 'lista_doctores.html', {'doctores': doctores})
