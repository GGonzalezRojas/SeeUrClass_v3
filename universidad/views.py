import boto3
from boto3.dynamodb.conditions import Key, Attr
from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse
from universidad.models import *
from usuarios.views import obtener_cursos
from django.http import HttpResponseRedirect

def crear_alumno(request):
    carreras = Carrera.objects.all()
    if request.method == 'POST':
        rut = request.POST.get('rut')
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        imagen = request.POST.get('imagen')
        pk_carrera = request.POST.get('select')
        guardar_nuevo_alumno(rut, nombre, apellido, pk_carrera, imagen)
    return render(request, 'alumnos/crear_alumno.html', {'carreras': carreras})


def guardar_nuevo_alumno(rut, nombre, apellido, pk_carrera, imagen):
    carrera = Carrera.objects.get(id=pk_carrera)
    nuevo_alumno = Alumno(imagen=imagen, carrera=carrera, rut=rut,
                          nombre=nombre, apellido=apellido)
    nuevo_alumno.save()


def editar_alumno(request):
    return render(request, 'alumnos/editar_alumno.html')


def borrar_alumno(request):
    return render(request, 'alumnos/borrar_alumno.html')


def mis_cursos(request):
    context = {}
    if request.method == 'POST':
        curso_pk = request.POST['curso_pk']
        return HttpResponseRedirect('/ver_alumnos_curso/{}'.format(curso_pk))
    cursos = obtener_cursos(request)
    context['cursos'] = cursos
    return render(request, 'profesores/mis_cursos.html', context)


def ver_alumnos_curso(request, pk):
    context = {}
    print(pk)
    # alumnos = AlumnoCurso.objects.filter(curso__id=pk)
    # if request.method == 'POST':
    #     print("Hola_2")
    return render(request, 'profesores/ver_alumnos_curso.html', {'pk':pk})


def asistencia_curso(request):
    asistencia('tics3', 'asistencia_curso')
    return render(request, 'profesores/asistencia_curso.html')


def asistencia(value, table_name):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(table_name)
    response = table.query(KeyConditionExpression=Key('curso').eq(value))
    items = response['Items']
    for item in items:
        print(item)
