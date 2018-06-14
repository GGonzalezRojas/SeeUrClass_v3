from django.urls import path
from . import views

urlpatterns = [
    path('crear_alumno/', views.crear_alumno, name='crear_alumno'),
    path('editar_alumno/', views.editar_alumno, name='editar_alumno'),
    path('borrar_alumno/', views.borrar_alumno, name='borrar_alumno'),
    path('mis_cursos/', views.mis_cursos, name='mis_cursos'),
    path('ver_alumnos_curso/', views.ver_alumnos_curso, name='ver_alumnos_curso')
]
