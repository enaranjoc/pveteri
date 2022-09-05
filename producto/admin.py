from django.contrib import admin
from .models import Marca, Producto, Servicio
# Register your models here.

class MarcaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'estado')

class ProductoAdmin(admin.ModelAdmin):
     list_display = ('id','nombre','marca','descripcion','stock','precio','estado')

class ServicioAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre','descripcion','precio', 'estado')

admin.site.register(Marca, MarcaAdmin)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Servicio, ServicioAdmin)


