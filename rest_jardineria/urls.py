from django.urls import path
from .views import listado_productos,detalle_producto

urlpatterns = [

path('listado_productos', listado_productos, name="listado_productos"),
path('detalle_producto/<id>',detalle_producto,name='detalle_producto'),

]