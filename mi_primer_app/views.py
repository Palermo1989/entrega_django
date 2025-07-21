from django.shortcuts import render, redirect, get_object_or_404
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
        return redirect('crear-doctor')  # Redirige a sí misma para mostrar el nuevo listado

    doctores = doctor.objects.all()
    return render(request, 'mi_primer_app/crear_doctor.html', {'doctores': doctores})

from django.shortcuts import render, redirect
from .forms import PacienteForm, EstudioForm

def crear_paciente(request):
    if request.method == 'POST':
        form = PacienteForm(request.POST)
        if form.is_valid():
            form.save()
            form = PacienteForm()  # formulario limpio
    else:
        form = PacienteForm()

    pacientes = Paciente.objects.all()
    return render(request, 'mi_primer_app/crear_paciente.html', {'form': form, 'pacientes': pacientes})

def modificar_paciente(request, pk):
    paciente = get_object_or_404(Paciente, id=pk)
    if request.method == 'POST':
        form = PacienteForm(request.POST, instance=paciente)
        if form.is_valid():
            form.save()
            return redirect('crear-paciente')
    else:
        form = PacienteForm(instance=paciente)
    return render(request, 'mi_primer_app/modificar_paciente.html', {'form': form})

def eliminar_paciente(request, pk):
    paciente = get_object_or_404(Paciente, id=pk)
    if request.method == 'POST':
        paciente.delete()
        return redirect('crear-paciente')
    return render(request, 'mi_primer_app/eliminar_paciente.html', {'paciente': paciente})

def crear_estudio(request):
    if request.method == 'POST':
        form = EstudioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('crear-estudio')  # Redirigir para evitar repost
    else:
        form = EstudioForm()

    estudios = Estudio.objects.all().order_by('-fecha')
    return render(request, 'mi_primer_app/crear_estudio.html', {'form': form, 'estudios': estudios})

    # Vista para editar un estudio
def editar_estudio(request, pk):
    estudio = get_object_or_404(Estudio, pk=pk)
    if request.method == 'POST':
        form = EstudioForm(request.POST, instance=estudio)
        if form.is_valid():
            form.save()
            return redirect('crear-estudio')
    else:
        form = EstudioForm(instance=estudio)
    return render(request, 'mi_primer_app/modificar_estudio.html', {'form': form})

# eliminar_estudio
def eliminar_estudio(request, pk):
    estudio = get_object_or_404(Estudio, pk=pk)
    if request.method == 'POST':
        estudio.delete()
        return redirect('crear-estudio')
    return render(request, 'mi_primer_app/eliminar_estudio.html', {'estudio': estudio})

