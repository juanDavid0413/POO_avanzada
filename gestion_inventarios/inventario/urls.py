from django.urls import path
from .views import listar_productos, agregar_producto, editar_producto, eliminar_producto

urlpatterns = [
    path('productos/', listar_productos, name='listar_productos'),
    path('productos/agregar/', agregar_producto, name='agregar_producto'),
    path('productos/editar/<int:pk>/', editar_producto, name= 'editar_producto'),
    path('productos/eliminar/<int:pk/', eliminar_producto, name= 'eliminar_producto'),
]