from django.contrib import admin
from .models import Facultad, Carrera, Curso


admin.site.register(Facultad)
admin.site.register(Carrera)
admin.site.register(Curso)