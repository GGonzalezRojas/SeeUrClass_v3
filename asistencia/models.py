from django.db import models
from django.apps import apps
from universidad.models import Carrera, Curso


class Imagen(models.Model):
    ruta_imagen = models.ImageField(null=True, default='rutaimagen')


class Alumno(models.Model):
    #Carrera = apps.get_model('universidad', 'Carrera')
    imagen = models.OneToOneField(Imagen, null=True, on_delete=models.CASCADE)
    carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE)
    rut = models.CharField(max_length=10, unique=True, null=False, default='11111111-1')
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)

    def __str__(self):
        return 'Nombre: {nombre} {apellido}'.format(nombre=self.nombre, apellido=self.apellido)


class Asistencia(models.Model):
    alumno = models.OneToOneField(Alumno, on_delete=models.CASCADE, related_name='alumno')
    fecha = models.DateField(auto_now=True)
    dispositivo = models.CharField(max_length=50)

    def __str__(self):
        return 'Asistencia de: {alumno} {curso}'.format(alumno=self.alumno, curso=self.curso)


class AsistenciaCurso(models.Model):
    curso = models.OneToOneField(Curso, on_delete=models.CASCADE, related_name='curso')
    asistencia = models.OneToOneField(Asistencia, on_delete=models.CASCADE, related_name='asistencia')

    def __str__(self):
        return 'Asistencia curso: {curso}'.format(curso=self.curso)