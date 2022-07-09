from dataclasses import fields
from pyexpat import model
from django import forms
from django.forms import ModelForm
from .models import Producto, Categoria
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


#Se crea la clase de producto
class FormularioPro(ModelForm):
    class Meta:
        model=Producto
        fields= ['id', 'nombre', 'descripcion', 'precio', 'imagen', 'categoria']
    
#Se crea la clase Categoria

class FormularioCat(ModelForm):
    class Meta:
        model= Categoria
        fields=['idCategoria', 'NombreCategoria']

#Creacionb de usuario
class CreacionDeUsuario(UserCreationForm):
    
    class Meta :
        model = User
        fields =  ['username',"first_name", "last_name","email" , "password1", "password2"]

#Login de usuario
class Login(AuthenticationForm):
    
    class Meta :
        model = User
    fields = ['username', "password"]