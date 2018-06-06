from django.db import models
from usuarios.models import Profesor


class Imagen(models.Model):
    ruta_imagen = models.ImageField(null=True, default='rutaimagen')


class Alumno(models.Model):
    rut = models.CharField(max_length=10, unique=True, null=False, default='11111111-1')
    imagen = models.OneToOneField(Imagen, null=True, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)

    def __str__(self):
        return 'Nombre: {nombre} {apellido}'.format(nombre=self.nombre, apellido=self.apellido)


class Curso(models.Model):
    profesor = models.OneToOneField(Profesor, null=False, on_delete=models.CASCADE, related_name='curso')
    alumnos = models.ForeignKey(Alumno, on_delete=models.CASCADE, related_name='curso')
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=100)
    fecha_creacion = models.DateField(auto_now=True)

    def __str__(self):
        return 'Nombre: {nombre} {codigo}'.format(nombre=self.nombre, codigo=self.codigo)


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
