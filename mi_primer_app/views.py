from django.shortcuts import render, redirect
from .models import doctor, Paciente, Estudio
from .forms import PacienteForm, EstudioForm
from django.http import HttpResponse


def inicio(request):
    return render(request, 'mi_primer_app/inicio.html')


def saludo(request):
    return HttpResponse("¡Hola, mundo!")


def saludo_con_template(request):
    return render(request, 'mi_primer_app/saludo.html')


def crear_doctor(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        edad = request.POST.get('edad')
        fecha_nacimiento = request.POST.get('fecha_nacimiento')
        especialidad = request.POST.get('especialidad')

        nuevo_doctor = doctor(
            nombre=nombre,
            apellido=apellido,
            edad=edad,
            fecha_nacimiento=fecha_nacimiento,
            especialidad=especialidad
        )
        nuevo_doctor.save()
        return redirect('inicio')

    return render(request, 'mi_primer_app/crear_doctor.html')

from django.shortcuts import render, redirect
from .forms import PacienteForm, EstudioForm

def crear_paciente(request):
    if request.method == 'POST':
        form = PacienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_paciente')
    else:
        form = PacienteForm()
    return render(request, 'mi_primer_app/crear_paciente.html', {'form': form})


def crear_estudio(request):
    if request.method == 'POST':
        form = EstudioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = EstudioForm()
    return render(request, 'mi_primer_app/crear_estudio.html', {'form': form})


def lista_paciente(request):
    pacientes = Paciente.objects.all()
    return render(request, 'mi_primer_app/paciente.html', {'pacientes': pacientes})


def buscar_paciente(request):
    if request.method == 'GET':
        nombre = request.GET.get('nombre', '')
        pacientes = Paciente.objects.filter(nombre__icontains=nombre)
        return render(request, 'mi_primer_app/paciente.html', {'pacientes': pacientes, 'nombre': nombre})
