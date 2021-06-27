from rest_framework import serializers
from PaginaWeb.models import Producto


class ProductoSerializer (serializers.ModelSerializer):

  class Meta: 
    model = Producto
    fields = ['marca','formato','codigo','nombre','valor','imagen','categoriapro',]