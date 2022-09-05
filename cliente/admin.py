from django.contrib import admin
from .models import Cliente, Especie, Raza, Mascota
# Register your models here.

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'apellido','cedula','email','direccion','telefono','usuario','contraseña')

class EspecieAdmin(admin.ModelAdmin):
    list_display = ('id','descripcion')

class RazaAdmin(admin.ModelAdmin):
    list_display = ('id', 'id_Especie','nombre_Raza')

class MascotaAdmin(admin.ModelAdmin):
    list_display = ('id', 'id_raza', 'id_cliente','nombre','fechaNaciemiento','sexo','color','imagen')


admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Especie, EspecieAdmin)
admin.site.register(Raza, RazaAdmin)
admin.site.register(Mascota, MascotaAdmin)