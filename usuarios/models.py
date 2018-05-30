from django.db import models
from django.conf import settings


class Administrador(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='administrador')
    rut = models.CharField(max_length=10, null=False, unique=True, default='111111111-1')

    def __str__(self):
        return 'Administrador : {username}'.format(username=self.user.username)


class Profesor(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profesor')
    rut = models.CharField(max_length=10, null=False, unique=True, default='111111111-1')

    def __str__(self):
        return 'Profesor: {username}'.format(username=self.user.username)
