from django.urls import path
from .views import listado_productos,detalle_producto

urlpatterns = [

path('listado-productos', listado_productos,name="listado_productos"),
path('detalle-producto/<id>',detalle_producto,name='detalle_producto'),

]