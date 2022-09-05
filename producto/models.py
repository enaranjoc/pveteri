from django.db import models

# Create your models here.
class Marca(models.Model):
    nombre = models.CharField(max_length=200, unique=True)
    estado = models.BooleanField(default=True)
    
    def __str__(self):
        return self.Mar_nombre