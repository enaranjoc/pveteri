from django.db import models

# Create your models here.
class Cliente(models.Model):
    #id_TipoUsuario = models.ForeignKey(TipoUsuario, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    cedula = models.CharField(max_length=10, unique=True)
    email = models.CharField(max_length=50, unique=True)
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=10, unique=True)
    usuario = models.CharField(max_length=50, unique=True)
    contraseña = models.CharField(max_length=50, unique=True) #ojo

 
    def __str__(self):
        return self.nombre

class Especie(models.Model):
    descripcion = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.descripcion

class Raza(models.Model):
    id_Especie = models.ForeignKey(Especie, on_delete=models.CASCADE)
    nombre_Raza = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.nombre_Raza
        
sleccionar_sexo = (
    ('H', 'Hembra'),
    ('M', 'Macho'),
)


class Mascota(models.Model):
    id_raza = models.ForeignKey(Raza, on_delete=models.CASCADE)
    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)
    fechaNaciemiento = models.DateField()
    sexo = models.CharField(max_length=10, choices=sleccionar_sexo)
    color = models.CharField(max_length=50)
    # foto = models.ImageField(upload_to='photos/products') #ojo
    imagen = models.ImageField(upload_to='imagenes/mascotas/%Y/%m/%d/')

    
    def __str__(self):
        return self.nombre