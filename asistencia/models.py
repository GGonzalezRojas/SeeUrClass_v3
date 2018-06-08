from django.db import models
from universidad.models import Curso, Carrera


class Imagen(models.Model):
    ruta_imagen = models.ImageField(null=True, default='rutaimagen')


class Alumno(models.Model):
    imagen = models.OneToOneField(Imagen, null=True, on_delete=models.CASCADE)
    carrera = models.OneToOneField(Carrera, on_delete=models.CASCADE)
    rut = models.CharField(max_length=10, unique=True, null=False, default='11111111-1')
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)

    def __str__(self):
        return 'Nombre: {nombre} {apellido}'.format(nombre=self.nombre, apellido=self.apellido)


class Asistencia(models.Model):
    curso = models.OneToOneField(Curso, on_delete=models.CASCADE)
    alumno = models.OneToOneField(Alumno, on_delete=models.CASCADE)
    fecha = models.DateField(auto_now=True)

    def __str__(self):
        return 'Asistencia de: {alumno} {curso}'.format(alumno=self.alumno, curso=self.curso)
