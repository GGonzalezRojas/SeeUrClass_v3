from django.contrib import admin
from .models import *


admin.site.register(Facultad)
admin.site.register(Carrera)
admin.site.register(Curso)
admin.site.register(Alumno)
admin.site.register(AlumnoCurso)