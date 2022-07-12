

# Create your views here.
from django.shortcuts import render
from core.cart import Cart
from core.form import FormularioPro, FormularioCat,CreacionDeUsuario,Login,User
from .models import Producto,Categoria
from rest_AmigosP.viewslogin import login
from django.contrib.auth import authenticate, login
from django.contrib import messages
from email import message
from pyexpat.errors import messages
from django.shortcuts import redirect, render
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required #indica nivel de permisos
from django.contrib.auth.mixins import PermissionRequiredMixin 
from django.views.generic.base import TemplateView

# Create your views here.
class IndexView(TemplateView):
    template_name = 'core/index.html'
    
def home(request):

    return render(request, 'core/index.html')
    
@permission_classes((IsAuthenticated, ))
def Productos(request):
    #Se define objeto para obtener los productos
    #Se puede utilizar Producto.object.all() o 'select * from Producto'
    productos = Producto.objects.all()

    #Se cargan los objetos obtenidos en la variable
    contexto = {
        'producto' : productos
    }
    return render(request, 'core/productos.html', contexto)

@login_required
@permission_classes((IsAdminUser,))
#Agregar Productos
def AgregarPro(request):
    
    contexto ={
        'producto' : FormularioPro()
    }

    #Se verifican los datos de producto
    if request.method == 'POST':
        #S recuperan los datos
        producto = FormularioPro(request.POST, request.FILES)
        #validacion de formulario
        if producto.is_valid:
            producto.save()
            contexto['mensaje'] = "Creado correctamente"
            return redirect(to='Productos')
    return render(request, 'core/AgregarPro.html', contexto)

    #eliminacion de producto
@login_required
def del_producto(request, id):
    #se usara la id para identificar el producto borrado
            producto = Producto.objects.get(id = id)
            #se elimina el producto que coincida con su id
            producto.delete()
            #redireccion a la pagina de productos
            return redirect(to= 'Productos')

@login_required
@permission_required((IsAuthenticated,IsAdminUser))
#Agregar una categoria
def AgregarCat(request):

    contexto ={
        'categoria': FormularioCat()
    }

        #Se verifican los datos de categoeia
    if request.method == 'POST':
        #S recuperan los datos
        categoria = FormularioCat(request.POST)
        #validacion de formulario
        if categoria.is_valid:
            categoria.save()
            contexto['mensaje'] = "Creado correctamente"
            return redirect(to='Productos')
    return render(request, 'core/agregarCat.html', contexto)

@login_required
#Modificar un producto
def ModificarPro(request, id):
    #rescatar producto por id
    producto = Producto.objects.get(id = id)
    #Se agrega al contexto
    contexto = {
        'form': FormularioPro(instance=producto)
    }
    #Se verifica que el metodo sea post 
    if request.method == 'POST':
        formulario = FormularioPro(data=request.POST, instance=producto)
        #validamos
        if formulario.is_valid():
            formulario.save()
            contexto['mensaje'] ="Producto Modificado"
            return redirect(to='Productos')
    return render(request, 'core/ModificarPro.html', contexto)
            
#para el registro de usuario
def Registro(request):
    data = {
        'form': CreacionDeUsuario()
    }
    if request.method ==  'POST':
        formulario = CreacionDeUsuario(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username = formulario.cleaned_data["username"], password = formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "Registro completado con exito")
            #redireccion
            return redirect(to='iniSesion')
        data["form"] = formulario
    return render(request , 'core/Registro.html', data)
@login_required
@permission_required('Vendedores')
def Admin(request):
        #Se define objeto para obtener los productos
    #Se puede utilizar Producto.object.all() o 'select * from Producto'
    usuarios = User.objects.all()

    #Se cargan los objetos obtenidos en la variable
    contexto = {
        'form' : usuarios
    }

    return render(request, 'core/VistaAdmin', contexto)

#definir view carro
def Carro(request):
    #obtiene los productos
    productos = Producto.objects.all()
    contexto = {
        'producto' : productos
    }
    return render(request, 'core/Carro.html', contexto )

#agregar al carrito
def agrega_carro(request, id):
    cart = Cart(request)
    producto = Producto.objects.get(id = id)
    cart.add(producto)
    return redirect(to = "Carro")

#elimiar del carro
def del_carro(request, id):
    cart = Cart(request)
    producto = Producto.objects.get(id = id)
    cart.remove(producto)
    return redirect(to = "Carro")

#restar
def res_carro(request, id):
    cart = Cart(request)
    producto = Producto.objects.get(id = id)
    cart.decrement(producto)
    return redirect(to = "Carro")

#limpiar carro
def limpiar_carro(request):
    cart = Cart(request)
    cart.clear()
    return redirect("Carro")


