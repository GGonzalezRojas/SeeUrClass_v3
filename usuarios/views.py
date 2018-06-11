from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from universidad.models import *


@login_required(login_url='/login/')
def dashboard(request):
    context = {}
    nombre, apellido = obtener_nombre_apellido(request)
    numero_alumnos = obtener_alumnos(request)
    cursos = obtener_cursos(request)
    context['nombre_profesor'] = nombre
    context['apellido_profesor'] = apellido
    context['cursos'] = cursos
    context['numero_alumnos'] = numero_alumnos
    return render(request, 'profesor/dashboard.html', context)


def obtener_nombre_apellido(request):
    usuario = request.user
    profesor = Profesor.objects.get(user__username=usuario)
    return profesor.user.first_name, profesor.user.last_name


def obtener_cursos(request):
    usuario = request.user
    cursos = Curso.objects.filter(profesor__user__username=usuario)
    return cursos


def obtener_alumnos(request):
    cursos = obtener_cursos(request)
    alumnos = []
    for curso in cursos:
        alumnos.append(Alumno.objects.filter(carrera__cursos=curso))
    return len(alumnos)

@login_required(login_url='/admin_login/')
def admin_dashboard(request):
    return render(request, 'administrador/admin_dashboard.html')


def admin_login(request):
    if request.method == 'POST':
        user = authenticate_user(request)
        if user is None:
            messages.error(request, 'Nombre de usuario o contraseña incorrectos')
        else:
            if user.is_active:
                django_login(request, user)
                return redirect(reverse('admin_dashboard'))
            else:
                messages.error(request, 'Usuario no activo')
    return render(request, 'administrador/admin_login.html')


def admin_logout(request):
    django_logout(request)
    return redirect(reverse('admin_login'))


def login(request):
    if request.method == 'POST':
        user = authenticate_user(request)
        if user is None:
            messages.error(request, 'Nombre de usuario o contraseña incorrectos')
        else:
            if user.is_active:
                django_login(request, user)
                return redirect(reverse('dashboard'))
            else:
                messages.error(request, 'El usuario no está activo')
    return render(request, 'profesor/login.html')


def logout(request):
    django_logout(request)
    return redirect(reverse('login'))


def authenticate_user(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(username=username, password=password)
    return user


def login_if_active(request, user):
    if user.is_active:
        django_login(request, user)
        return redirect(reverse('dashboard'))
    else:
        messages.error(request, 'El usuario no está activo')
