from django.db import models




class doctor(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    edad = models.IntegerField()
    fecha_nacimiento = models.DateField()
    especialidad = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Paciente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    edad = models.IntegerField()
    obra_social = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nombre


class Estudio(models.Model):
    nombre = models.CharField(max_length=100)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    fecha = models.DateField()
    urgencia = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.nombre} {self.paciente}."
