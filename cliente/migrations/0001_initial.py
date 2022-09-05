# Generated by Django 4.1 on 2022-09-05 07:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('cedula', models.CharField(max_length=10, unique=True)),
                ('email', models.CharField(max_length=50, unique=True)),
                ('direccion', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=10, unique=True)),
                ('usuario', models.CharField(max_length=50, unique=True)),
                ('contraseña', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Especie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Raza',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_Raza', models.CharField(max_length=200, unique=True)),
                ('id_Especie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cliente.especie')),
            ],
        ),
        migrations.CreateModel(
            name='Mascota',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('fechaNaciemiento', models.DateField()),
                ('sexo', models.CharField(choices=[('H', 'Hembra'), ('M', 'Macho')], max_length=10)),
                ('color', models.CharField(max_length=50)),
                ('imagen', models.ImageField(upload_to='imagenes/mascotas/%Y/%m/%d/')),
                ('id_cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cliente.cliente')),
                ('id_raza', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cliente.raza')),
            ],
        ),
    ]
