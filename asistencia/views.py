import boto3
from boto3.dynamodb.conditions import Key, Attr
from django.shortcuts import render
from usuarios.views import obtener_cursos


def asistencia_cursos(request):
    #asistencia('tics3', 'asistencia_curso')
    context = {}

    return render(request, 'asistencia/asistencia_cursos.html', context)


def asistencia(value, table_name):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(table_name)
    response = table.query(KeyConditionExpression=Key('curso').eq(value))
    items = response['Items']
    for item in items:
        print(item)