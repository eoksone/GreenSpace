from django.urls import path
from django.urls.conf import include

from django.urls.resolvers import URLPattern
from .views import home,cuenta,registrar,compost,mulchoficial,sustrato,agregar,listadopro,modificar,eliminar
from django.conf.urls.static import static 
from django.conf import settings

urlpatterns =[
path ('',home,name="home"),
path ('cuenta/',cuenta,name="cuenta"),
path ('registrar/',registrar,name="registrar"),
path ('compost/',compost,name="compost"),
path ('mulchoficial/',mulchoficial,name="mulchoficial"),
path ('sustrato/',sustrato,name="sustrato"),
path ('agregar/',agregar,name="agregar"),
path ('listadopro/',listadopro,name="listadopro"),
path ('modificar/<id>/',modificar,name="modificar"),
path('eliminar/<id>/', eliminar, name='eliminar'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)