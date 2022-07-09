from django.urls import path
from rest_AmigosP.views import lista_productos,Detalle_producto
from rest_AmigosP.viewslogin import login

urlpatterns = [
    path('lista_productos', lista_productos, name="lista_productos"),
    path('Detalle_producto/<ID>', Detalle_producto ,name="Detalle_producto"),
    path('login', login, name="login"),
]