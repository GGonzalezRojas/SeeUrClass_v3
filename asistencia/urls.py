from django.urls import path
from . import views

urlpatterns = [
    path('estadisticas_cursos/', views.estadisticas_cursos, name='estadisticas_cursos'),
    path('listas_asistencia/', views.listas_asistencia, name='listas_asistencia')
    ]
