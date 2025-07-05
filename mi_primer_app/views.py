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
