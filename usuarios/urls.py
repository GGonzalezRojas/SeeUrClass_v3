from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('admin_login/', views.admin_login, name='admin_login'),
    path('admin_logout/', views.admin_logout, name='admin_logout'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('crear_alumno/', views.crear_alumno, name='crear_alumno'),
    path('editar_alumno/', views.editar_alumno, name='editar_alumno'),
    path('borrar_alumno/', views.borrar_alumno, name='borrar_alumno')
]
