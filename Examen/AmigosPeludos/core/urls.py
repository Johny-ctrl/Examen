from unicodedata import name
from django.urls import path
from .views import home, Productos, AgregarCat, AgregarPro,Registro,del_producto,ModificarPro,Admin

urlpatterns = [
    path('', home, name='home'),
    path('Productos',Productos, name='Productos'),
    path('AgregarProducto', AgregarPro, name= 'AgregarPro'),
    path('AgregarCat', AgregarCat, name='AgregarCat'),
    path('Registro', Registro, name="Registro"),
    path('del_producto/<id>', del_producto, name="del_producto"),
    path('ModificarPro/<id>', ModificarPro , name="ModificarPro"),
    path('Admin', Admin, name="Admin"),
]