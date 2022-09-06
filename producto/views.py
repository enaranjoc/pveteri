from django.shortcuts import render
from .models import *

# Create your views here.



def producto(request):
    listaProductos = Producto.objects.all()
    return render(request, 'producto.html', {'productos': listaProductos})

def marca(request):
    listarMarca = Marca.objects.all()
    return render(request, 'producto.html', {'marcas': listarMarca})