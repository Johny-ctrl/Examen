
from django.urls import path
from .views import home, Productos, AgregarCat, AgregarPro,Registro,del_producto,ModificarPro,Admin,Carro,agrega_carro,del_carro,res_carro,limpiar_carro

urlpatterns = [
    path('', home, name='home'),
    path('Productos',Productos, name='Productos'),
    path('AgregarProducto', AgregarPro, name= 'AgregarPro'),
    path('AgregarCat', AgregarCat, name='AgregarCat'),
    path('Registro', Registro, name="Registro"),
    path('del_producto/<id>', del_producto, name="del_producto"),
    path('ModificarPro/<id>', ModificarPro , name="ModificarPro"),
    path('Admin', Admin, name="Admin"),
    path('Carro', Carro, name="Carro"),
    path('agrega_carro/<id>',agrega_carro, name="agrega_carro"),
    path('del_carro/<pid',del_carro, name="del_carro"),
    path('res_carro/<id>',res_carro, name="res_carro"),
    path('limpiar_carro/<id>',limpiar_carro, name="limpiar_carro"),






]