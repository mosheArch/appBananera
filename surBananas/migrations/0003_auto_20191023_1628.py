# Generated by Django 2.2.6 on 2019-10-23 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('surBananas', '0002_auto_20191023_1628'),
    ]

    operations = [
        migrations.AlterField(
            model_name='areas',
            name='fase',
            field=models.CharField(blank=True, choices=[('', 'Fases'), ('Unidad de Empaque', 'Unidad de Empaque'), ('Unidad de Producción', 'Unidad de Producción')], default='', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='areas',
            name='tiposRiesgo',
            field=models.CharField(blank=True, choices=[('Físico y Quimico', 'Físico y Quimico'), ('Quimico', 'Quimico'), ('', 'Tipos de riesgo'), ('Físico', 'Físico')], default='', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='empleados',
            name='nacionalidad',
            field=models.CharField(choices=[('Mexicana', 'Mexicana'), ('', 'Nacionaidad'), ('Extranjero', 'Extranjero')], default='', max_length=20),
        ),
    ]
