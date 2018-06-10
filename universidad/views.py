from django.shortcuts import render
from universidad.models import Alumno, Carrera

def crear_alumno(request):
    if request.method == 'POST':
        rut = request.POST.get('rut')
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        imagen = request.POST.get('imagen')
        cod_carrera = request.POST.get('select')
        guardar_nuevo_alumno(rut, nombre, apellido, cod_carrera, imagen)
    return render(request, 'alumnos/crear_alumno.html')


def guardar_nuevo_alumno(rut, nombre, apellido, cod_carrera, imagen):
    carrera = Carrera.objects.get(codigo=cod_carrera)
    nuevo_alumno = Alumno(imagen=imagen, carrera=carrera, rut=rut,
                          nombre=nombre, apellido=apellido)
    nuevo_alumno.save()


def editar_alumno(request):
    return render(request, 'alumnos/editar_alumno.html')


def borrar_alumno(request):
    return render(request, 'alumnos/borrar_alumno.html')


