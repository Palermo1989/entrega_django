from django.shortcuts import render, redirect
from .models import doctor, Paciente, Estudio
from .forms import Pacienteform, EstudioForm
from django.http import HttpResponse


def inicio(request):
    return render(request, 'mi_primer_app/inicio.html')


def saludo(request):
    return HttpResponse("¡Hola, mundo!")


def saludo_con_template(request):
    return render(request, 'mi_primer_app/saludo.html')


def crear_doctor(request, nombre):
    if nombre is not None:
        nuevo_doctor = doctor(
            nombre=nombre,
            apellido="ApellidoEjemplo",
            edad=30,
            fecha_nacimiento="1993-01-01",
            especialidad="Primo"
        )
        nuevo_doctor.save()
    return render(request, "mi_primer_app/crear_doctor.html", {"nombre": nombre})


def crear_paciente(request):
    if request.method == 'POST':
        form = Pacienteform(request.POST)
        if form.is_valid():
            nuevo_paciente = Paciente(
                nombre=form.cleaned_data['nombre'],
                apellido=form.cleaned_data['apellido'],
                direccion=form.cleaned_data['direccion'],
                edad=form.cleaned_data['edad'],
                obra_social=form.cleaned_data['obra_social'],
            )
            nuevo_paciente.save()
            return redirect('lista_paciente')
    else:
        form = Pacienteform()
    return render(request, 'mi_primer_app/crear_paciente.html', {'form': form})


def crear_estudio(request):
    if request.method == 'POST':
        form = EstudioForm(request.POST)
        if form.is_valid():
            nuevo_estudio = Estudio(
                nombre=form.cleaned_data['nombre'],
                paciente=form.cleaned_data['paciente'],
                fecha=form.cleaned_data['fecha'],
                urgencia=form.cleaned_data['urgencia'],
            )
            nuevo_estudio.save()
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
