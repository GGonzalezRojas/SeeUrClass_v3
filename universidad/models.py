from django.db import models
from usuarios.models import Profesor
from asistencia.models import Alumno, Asistencia


class Curso(models.Model):
    profesor = models.OneToOneField(Profesor, null=False, on_delete=models.CASCADE, related_name='profesor')
    alumnos = models.ForeignKey(Alumno, on_delete=models.CASCADE, related_name='alumnos')
    asistencia = models.ForeignKey(Asistencia, on_delete=models.CASCADE, related_name='asistencia')
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=100)
    seccion = models.CharField(max_length=50)
    semestre = models.CharField(max_length=50)
    fecha = models.DateField(auto_now=True)

    def __str__(self):
        return 'Curso: {nombre} {codigo}'.format(nombre=self.nombre, codigo=self.codigo)


class Carrera(models.Model):
    cursos = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name='carrera')
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=100)

    def __str__(self):
        return 'Nombre: {nombre}'.format(nombre=self.nombre)


class Facultad(models.Model):
    carreras = models.ForeignKey(Carrera, on_delete=models.CASCADE, related_name='facultad')
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)

    def __str__(self):
        return 'Nombre: {nombre}'.format(nombre=self.nombre)
