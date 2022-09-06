from django.db import models

# Create your models here.
# Tabla marca
class Marca(models.Model):
    nombre = models.CharField(max_length=200, unique=True)
    estado = models.BooleanField(default=True)
    
    def __str__(self):
        return self.nombre

# Tabla producto
class Producto(models.Model):
    nombre = models.CharField(max_length=200, unique=True)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    descripcion = models.TextField(max_length=500, blank=True)
    stock = models.IntegerField()
    precio = models.IntegerField()
    estado = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

class Servicio(models.Model):
    nombre = models.CharField(max_length=200, unique=True)
    descripcion = models.TextField(max_length=500, blank=True)
    precio = models.IntegerField()
    estado = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

        