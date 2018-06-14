from django.db import models
from usuarios.models import Profesor


class Curso(models.Model):
    profesor = models.ForeignKey(Profesor, null=False, on_delete=models.CASCADE, related_name='profesor')
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=100)
    seccion = models.CharField(max_length=50)
    semestre = models.CharField(max_length=50)
    fecha_creacion = models.DateField(auto_now=True)

    def __str__(self):
        return 'Curso: {nombre} {codigo}'.format(nombre=self.nombre, codigo=self.codigo)


class Carrera(models.Model):
    cursos = models.ManyToManyField(Curso, related_name='carrera')
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=100)

    def __str__(self):
        return 'Nombre: {nombre}'.format(nombre=self.nombre)


class Alumno(models.Model):
    imagen = models.ImageField(upload_to='fotos_alumnos', default ='fotos_alumnos/None/no-img.jpg', null=True)
    carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE, related_name='carrera')
    rut = models.CharField(max_length=10, unique=True, null=False, default='11111111-1')
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)

    def __str__(self):
        return 'Alumno: {nombre} {apellido}/{carrera}'.format(nombre=self.nombre, apellido=self.apellido, carrera=self.carrera.nombre)


class AlumnoCurso(models.Model):
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE, related_name='alumno_curso')
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name='curso_alumno')

    def __str__(self):
        return 'Alumnos en {curso} {alumno}'.format(curso=self.curso, alumno=self.alumno)


class Facultad(models.Model):
    carreras = models.ManyToManyField(Carrera, related_name='facultad')
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)

    def __str__(self):
        return 'Nombre: {nombre}'.format(nombre=self.nombre)
