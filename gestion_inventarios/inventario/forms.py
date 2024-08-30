from django import forms
from .models import Producto, Categoria, Proveedor

class ProductoForm(forms.modelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'categoria', 'proveedor', 'etiquetas', 'cantidad', 'precio', 'descripcion']



class CategoriaForm(forms.modelForm):
    class Meta:
        model = Categoria
        fields = ['nombre', 'descripcion']



class ProveedorForm(forms.modelForm):
    class Meta:
        model = Proveedor
        fields = ['nombre', 'contacto', 'telefono']