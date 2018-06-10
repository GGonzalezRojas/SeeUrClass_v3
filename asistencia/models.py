from django.db import models
from universidad.models import Curso, Alumno


class Asistencia(models.Model):
    alumno = models.OneToOneField(Alumno, on_delete=models.CASCADE, related_name='alumno')
    fecha = models.CharField(max_length=40)
    hora = models.CharField(max_length=40)
    rekog_value = models.CharField(max_length=40)
    dispositivo = models.CharField(max_length=50)

    def __str__(self):
        return 'Asistencia de: {alumno}{apellido}'.format(alumno=self.alumno.nombre, apellido=self.alumno.apellido)


class AsistenciaCurso(models.Model):
    curso = models.OneToOneField(Curso, on_delete=models.CASCADE, related_name='curso')
    asistencia = models.OneToOneField(Asistencia, on_delete=models.CASCADE, related_name='asistencia')

    def __str__(self):
        return 'Asistencia curso: {curso} {alumno}'.format(curso=self.curso, alumno=self.asistencia.alumno.nombre)
