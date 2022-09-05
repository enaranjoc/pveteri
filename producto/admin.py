from django.contrib import admin
from .models import Producto
# Register your models here.

class MarcaAdmin(admin.ModelAdmin):
    list_display = ('id', 'Nombre', 'Estado')

class ProductoAdmin(admin.ModelAdmin):
     list_display = ('id','Prod_nombre','Prod_marca','Prod_descripcion','Prod_stock','Prod_precio','Prod_estado')


admin.site.register(Marca, MarcaAdmin)
admin.site.register(Producto, ProductoAdmin)


