from django.db import models

class Facultad(models.Model):
    carreras = models.ForeignKey(Carrera, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=40)
    direccion = models.CharField(max_length=40)

    def __str__(self):
        return 'Nombre: {nombre}'.format(nombre=self.nombre)


class Carrera(models.Model):
    cursos = models.ForeignKey(Curso, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=40)
    codigo = models.CharField(max_length=40)

    def __str__(self):
        return 'Nombre: {nombre}'.format(nombre=self.nombre)

class Curso(models.Model):
    alumnos = models.ForeignKey(Alumnos, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=40)
    codigo = models.CharField(max_length=40)

    def __str__(self):
        return 'Nombre: {nombre} {codigo}'.format(nombre=self.nombre, codigo=self.codigo)

class Alumnos(models.Model):
    rut = models.CharField(max_length=10 , unique=True, null=False)
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)

    def __str__(self):
        return 'Nombre: {nombre} {apellido}'.format(nombre=self.nombre, apellido=self.apellido)
