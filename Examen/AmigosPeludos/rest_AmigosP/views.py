from ast import Return
from urllib import response
from django.shortcuts import render
from rest_framework import response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from core.models import Producto,Categoria
from .serializers import FormularioProSerializer, FormularioCatSerializer
from rest_framework import status

#autenticacion
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated,IsAdminUser
# Create your views here.
@csrf_exempt
@api_view(['GET', 'POST'])
@permission_classes((IsAuthenticated,))
def lista_productos(request):
    #Para listar todos los productos
    if request.method=='GET':
        producto= Producto.objects.all()
        serializer = FormularioProSerializer(producto, many=True)
        return Response(serializer.data)#Se retorna una lista serializada en JSON

        #agregar un producto por JSON
    elif request.method=='POST':
        data=JSONParser().parse(request)
        serializer=FormularioProSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#mostrar detalles de un producto en especial
@api_view(['GET','PUT', 'DELETE'])
@permission_classes((IsAdminUser))
def Detalle_producto(request,ID):
    try: #filtro producto por id
        producto= Producto.objects.get(id = ID)
    except Producto.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=='GET': #Traer #serializo UN Producto (el filtrado por su id)
        serializer=FormularioProSerializer(producto)
        return Response(serializer.data)
    if request.method=='PUT': #Modificar
        data=JSONParser().parse(request)
        serializer=FormularioProSerializer(producto, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method=='DELETE': #Borrar
        producto.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



# Create your views here.
