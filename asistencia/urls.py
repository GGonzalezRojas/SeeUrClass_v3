from django.urls import path
from . import views

urlpatterns = [
    path('asistencia_cursos/', views.asistencia_cursos, name='asistencia_cursos')
    ]
