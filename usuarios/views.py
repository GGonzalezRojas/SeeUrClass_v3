from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse


@login_required(login_url='/login/')
def dashboard(request):
    return render(request, 'profesor/dashboard.html')


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
