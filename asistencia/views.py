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
    print(asistencia)
    nueva_sistencia = Asistencia()


def query_item(
    self, table_name, sort_key, partition_key,
    index_name=None, total_items=None, start_key=None,
    table=None
):
        """
        Query for an item with or without using global secondary index
        PARAMS:
        @table_name: name of the table
        @sort_key: Dict containing key and val of sort key
        e.g. {'name': 'uuid', 'value': '077f4450-96ee-4ba8-8faa-831f6350a860'}
        @partition_key: Dict containing key and val of partition key
        e.g. {'name': 'date', 'value': '2017-02-12'}
        @index_name (optional): Name of the Global Secondary Index
        """
        if not table:
            dynamodb = self.conn
            table = dynamodb.Table(table_name)
        sk = sort_key['name']
        skv = sort_key['value']
        pk = partition_key['name']
        pkv = partition_key['value']
        if not start_key:
            if index_name:
                response = table.query(
                    IndexName=index_name,
                    KeyConditionExpression=Key(sk).eq(skv) &
                    Key(pk).eq(pkv)
                )
            else:
                response = table.query(
                    KeyConditionExpression=Key(sk).eq(skv) &
                    Key(pk).eq(pkv)
                )
        else:
            if index_name:
                response = table.query(
                    IndexName=index_name,
                    KeyConditionExpression=Key(sk).eq(skv) &
                    Key(pk).eq(pkv),
                    ExclusiveStartKey=start_key
                )
            else:
                response = table.query(
                    KeyConditionExpression=Key(sk).eq(skv) &
                    Key(pk).eq(pkv),
                    ExclusiveStartKey=start_key
                )
        if not total_items:
            total_items = response['Items']
        else:
            total_items.extend(response['Items'])
        if response.get('LastEvaluatedKey'):
            start_key = response['LastEvaluatedKey']
            return_items = self.query_item(
                table_name=table_name, sort_key=sort_key,
                partition_key=partition_key, total_items=total_items,
                start_key=start_key, table=table
            )
            return return_items
        else:
            return total_items


def estadisticas_cursos(request):
    obtener_asistencia('tic3_v6')
    context = {}
    return render(request, 'asistencia/estadisticas_cursos.html', context)


def obtener_asistencia(table_name):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(table_name + 'assistance')
    response = table.query(KeyConditionExpression=Key('curso').eq(table_name))
    items = response['Items']
    guardar_asistencia(items)


def query_table(table_name, filter_key=None, filter_value=None):
    """
    Perform a query operation on the table. Can specify filter_key (col name) and its value to be filtered. Returns the response.
    """
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(table_name + 'assistance')
    if filter_key and filter_value:
        filtering_exp = Key(filter_key).eq(filter_value)
        response = table.query(KeyConditionExpression=filtering_exp)
    else:
        response = table.query()
    return response


def scan_table_allpages(table_name, filter_key=None, filter_value=None):
    """
    Perform a scan operation on table. Can specify filter_key (col name) and its value to be filtered. This gets all pages of results.
    Returns list of items.
    """
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(table_name + 'assistance')
    if filter_key and filter_value:
        filtering_exp = Key(filter_key).eq(filter_value)
        response = table.scan(FilterExpression=filtering_exp)
    else:
        response = table.scan()

    items = response['Items']
    while True:
        print (len(response['Items']))
        if response.get('LastEvaluatedKey'):
            response = table.scan(
                ExclusiveStartKey=response['LastEvaluatedKey'])
            items += response['Items']
        else:
            break

    return items


def detalle_asistencia(curso, curso_pk):
    numero_alumno = []
    curso = Curso.objects.get(id=curso_pk)
    alumnos_asistencia = [index.asistencia for index in AsistenciaCurso.objects.filter(curso=curso)]
    i = 1
    for asistencia in alumnos_asistencia:
        numero_alumno.append((i, asistencia))
        i += 1
    return curso, numero_alumno
