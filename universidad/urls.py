from django.urls import path
from . import views

urlpatterns = [
    path('crear_alumno/', views.crear_alumno, name='crear_alumno'),
    path('editar_alumno/', views.editar_alumno, name='editar_alumno'),
    path('borrar_alumno/', views.borrar_alumno, name='borrar_alumno')
]
