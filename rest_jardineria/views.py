from django.shortcuts import render
from rest_framework import serializers, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import DataAndFiles, JSONParser
from django.views.decorators.csrf import csrf_exempt
from PaginaWeb.models import Producto
from .serializers import ProductoSerializer
@csrf_exempt
@api_view (['GET' , 'POST'])
def listado_productos (request):
 
    if request.method == 'GET':
        
        producto = Producto.objects.all ()
        serializers = ProductoSerializer (producto, many=True )
        return Response (serializers.data)
    elif request.method  == 'POST' :
        data = JSONParser ().parse(request)
        serializers = ProductoSerializer(data=data)
        if serializers.is_valid ():
            serializers.save ()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        else:
                return Response (serializers.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def detalle_producto(request,id):

    try:

        producto = Producto.objects.get(marca=id)

    except Producto.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


    if request.method == 'GET':

        serializers = ProductoSerializer(producto)

        return Response(serializers.data)

    if request.method == 'PUT':

        data = JSONParser().parse(request)

        serializers = ProductoSerializer(producto, data=data)

        if(serializers.is_valid()):

            serializers.save()

            return Response(serializers.data)

        else:

            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':

        producto.delete()

        return Response(status=status.HTTP_204_NOT_CONTENT)