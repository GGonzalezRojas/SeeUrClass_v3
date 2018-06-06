from django.contrib import admin
from .models import Facultad, Carrera, Curso, Alumno


admin.site.register(Facultad)
admin.site.register(Carrera)
admin.site.register(Curso)
admin.site.register(Alumno)
