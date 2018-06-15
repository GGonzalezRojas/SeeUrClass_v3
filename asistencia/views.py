import boto3
from boto3.dynamodb.conditions import Key, Attr
from django.shortcuts import render
from asistencia.models import AsistenciaCurso, Asistencia
from universidad.models import AlumnoCurso, Curso
from universidad.views import ver_alumnos_curso
from usuarios.views import obtener_cursos


def listas_asistencia(request):
    context = {}
    if request.method == 'POST':
        curso_pk = request.POST['curso_pk']
        curso, alumnos_asistencia = detalle_asistencia(request, curso_pk)
        context['curso'] = curso
        context['alumnos_asistencia'] = alumnos_asistencia
        return render(request, 'asistencia/detalle_asistencia.html', context)
    context['curso_cantidad'] = cantidad_alumnos_curso(request)
    return render(request, 'asistencia/listas_asistencia.html', context)


def cantidad_alumnos_curso(request):
    curso_cantidad = []
    cursos = obtener_cursos(request)
    for curso in cursos:
        curso_cantidad.append((curso, AlumnoCurso.objects.filter(curso=curso).count()))
    return curso_cantidad


def guardar_asistencia(asistencia):
    print(asistencia[0])
    nueva_sistencia = Asistencia()


def estadisticas_cursos(request):
    obtener_asistencia('tics3', 'asistencia_curso')
    context = {}
    return render(request, 'asistencia/estadisticas_cursos.html', context)


def obtener_asistencia(value, table_name):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(table_name)
    response = table.query(KeyConditionExpression=Key('curso').eq(value))
    items = response['Items']
    guardar_asistencia(items)


def detalle_asistencia(curso, curso_pk):
    numero_alumno = []
    curso = Curso.objects.get(id=curso_pk)
    alumnos_asistencia = [index.asistencia for index in AsistenciaCurso.objects.filter(curso=curso)]
    i = 1
    for asistencia in alumnos_asistencia:
        numero_alumno.append((i, asistencia))
        i += 1
    return curso, numero_alumno
