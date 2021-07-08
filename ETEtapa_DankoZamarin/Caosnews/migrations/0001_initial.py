# Generated by Django 3.2.3 on 2021-07-01 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Colaborador',
            fields=[
                ('rutColaborador', models.IntegerField(primary_key=True, serialize=False, verbose_name='Rut colaborador')),
                ('fotoColaborador', models.ImageField(upload_to='foto', verbose_name='Foto colaborador')),
                ('nomColaborador', models.CharField(max_length=60, verbose_name='Nombre colaborador')),
                ('fonoColaborador', models.IntegerField(verbose_name='Telefono colaborador')),
                ('dirColaborador', models.CharField(max_length=60, verbose_name='Dirección colaborador')),
                ('emailColaborador', models.EmailField(max_length=254, verbose_name='E-mail colaborador')),
                ('paisColaborador', models.CharField(max_length=60, verbose_name='País colaborador')),
                ('contrasenaColaborador', models.CharField(max_length=20, verbose_name='Contraseña')),
            ],
        ),
    ]
