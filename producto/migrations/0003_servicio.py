# Generated by Django 4.1 on 2022-09-05 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0002_rename_nombre_p_producto_nombre'),
    ]

    operations = [
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200, unique=True)),
                ('descripcion', models.TextField(blank=True, max_length=500)),
                ('precio', models.IntegerField()),
                ('estado', models.BooleanField(default=True)),
            ],
        ),
    ]
