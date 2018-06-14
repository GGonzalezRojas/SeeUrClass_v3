# Generated by Django 2.0.6 on 2018-06-14 18:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('asistencia', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asistencia',
            name='alumno',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='alumno', to='universidad.Alumno'),
        ),
        migrations.AlterField(
            model_name='asistenciacurso',
            name='asistencia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='asistencia', to='asistencia.Asistencia'),
        ),
        migrations.AlterField(
            model_name='asistenciacurso',
            name='curso',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='curso', to='universidad.Curso'),
        ),
    ]