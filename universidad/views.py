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
        lista_alumnos, curso = ver_alumnos_curso_v2(request, curso_pk)
        context['curso'] = curso
        context['lista_alumnos'] = lista_alumnos
        return render(request, 'profesores/ver_alumnos_curso.html', context)
        #return HttpResponseRedirect('/ver_alumnos_curso/{}'.format(curso_pk))
    cursos = obtener_cursos(request)
    context['cursos'] = cursos
    return render(request, 'profesores/mis_cursos.html', context)


def ver_alumnos_curso_v2(request, pk):
    context = {}
    curso = Curso.objects.get(id=pk)
    lista_alumnos = AlumnoCurso.objects.filter(curso=curso)
    return lista_alumnos, curso


def ver_alumnos_curso(request, context):
    return render(request, 'profesores/ver_alumnos_curso.html', context)
    '''context = {}
    print(pk)
    return render(request, 'profesores/ver_alumnos_curso.html', {'pk':pk})'''


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
