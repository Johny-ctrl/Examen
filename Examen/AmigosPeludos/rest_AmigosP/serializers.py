from dataclasses import field, fields
from rest_framework import serializers
from core.models import Producto, Categoria

#importar serializers
from rest_framework import serializers

#Se crea la clase de producto
class FormularioProSerializer(serializers.ModelSerializer):
    class Meta:
        model=Producto
        fields= ['id', 'nombre', 'descripcion', 'precio', 'imagen', 'categoria']
    
#Se crea la clase Categoria

class FormularioCatSerializer(serializers.ModelSerializer):
    class Meta:
        model= Categoria
        fields=['idCategoria', 'NombreCategoria']