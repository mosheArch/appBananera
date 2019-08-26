# Generated by Django 2.2.4 on 2019-08-25 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='empleados',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(blank=True, max_length=20, null=True)),
                ('apelidoPaterno', models.CharField(blank=True, max_length=20, null=True)),
                ('apelidoMaterno', models.CharField(blank=True, max_length=20, null=True)),
                ('edad', models.IntegerField(blank=True, null=True)),
                ('fechaNacimiento', models.DateField(blank=True, null=True)),
                ('numeroSeguroSocial', models.IntegerField(blank=True, null=True)),
                ('curp', models.CharField(blank=True, max_length=20, null=True)),
                ('rfc', models.CharField(blank=True, max_length=20, null=True)),
                ('estadoCivil', models.CharField(blank=True, max_length=20, null=True)),
                ('nacionalidad', models.CharField(blank=True, max_length=20, null=True)),
                ('area', models.CharField(blank=True, max_length=30, null=True)),
                ('labor', models.CharField(blank=True, max_length=20, null=True)),
                ('telefono', models.IntegerField(blank=True, null=True)),
                ('celular', models.IntegerField(blank=True, null=True)),
                ('correoElectronico', models.EmailField(blank=True, max_length=50, null=True)),
                ('domicilio', models.CharField(blank=True, max_length=200, null=True)),
                ('imagen', models.FileField(blank=True, null=True, upload_to='aquivalaruta')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]
