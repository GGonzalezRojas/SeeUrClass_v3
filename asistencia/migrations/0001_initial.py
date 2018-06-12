# Generated by Django 2.0.6 on 2018-06-12 19:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('universidad', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Asistencia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.CharField(max_length=40)),
                ('hora', models.CharField(max_length=40)),
                ('rekog_value', models.CharField(max_length=40)),
                ('dispositivo', models.CharField(max_length=50)),
                ('alumno', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='alumno', to='universidad.Alumno')),
            ],
        ),
        migrations.CreateModel(
            name='AsistenciaCurso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asistencia', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='asistencia', to='asistencia.Asistencia')),
                ('curso', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='curso', to='universidad.Curso')),
            ],
        ),
    ]
