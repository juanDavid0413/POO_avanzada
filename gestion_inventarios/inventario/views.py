from django.shortcuts import render, redirect
from .models import Producto
from .forms import ProductoForm

def listar_productos(request):
    productos = Producto.objects.all()
    return render(request, 'inventario/listar_productos.html', {'productos': productos})


def agregar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar:productos')
    else:
        form = ProductoForm()
    return render(request, 'inventario/agregar_producto.html', {'form':form})

def editar_producto(request, pk):
    producto = Producto.objects.get(pk=pk)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=Producto)
        if form.is_valid():
            form.save()
            return redirect('listar:productos')
    else:
        form = ProductoForm()
        instance = producto
    return render(request, 'inventario/agregar_producto.html', {'form':form})


def eliminar_producto(request, pk)
    producto = Producto.objects.get(pk=pk)
    if request.method == 'POST':
        producto.delete()
        return redirect('listar_productos')
    return render(request, 'inventario/eliminar_producto.html', {'producto':producto})    
            

# Create your views here.
