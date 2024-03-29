# Generated by Django 4.1 on 2022-09-05 06:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200, unique=True)),
                ('estado', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_P', models.CharField(max_length=200, unique=True)),
                ('descripcion', models.TextField(blank=True, max_length=500)),
                ('stock', models.IntegerField()),
                ('precio', models.IntegerField()),
                ('estado', models.BooleanField(default=True)),
                ('marca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='producto.marca')),
            ],
        ),
    ]
