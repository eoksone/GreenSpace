from django.shortcuts import render,redirect,get_object_or_404
from .models import Producto
from .forms import ProductoForm


# Create your views here.

def home (request):
    return render (request, 'paginaweb/index.html')

   
def cuenta (request):
    return render (request, 'paginaweb/cuenta.html')

def registrar (request):
    return render (request, 'paginaweb/registrar.html')


def compost (request):
    return render (request, 'PaginaWeb/compost.html')


def mulchoficial (request):

    producto = Producto.objects.all()
    data = {
        'producto' : producto
    }
    return render (request, 'PaginaWeb/mulchoficial.html',data)

def sustrato (request):
    return render (request, 'PaginaWeb/sustrato.html')




def listadopro(request):
    producto = Producto.objects.all()
   

    datos ={
        'producto':producto,
      
    }
    return render(request, 'PaginaWeb/listadopro.html', datos)

def eliminar(request, id):

    producto = Producto.objects.get(id = id)
    producto.delete()

    return redirect(to="listadopro")


def agregar(request):
    data = {
        'form' : ProductoForm()
    }
    if request.method == 'POST':
        formulario = ProductoForm(request.POST,files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Guardado Correctamente"
        else:
            formulario= ProductoForm()
    return render(request, 'PaginaWeb/agregar.html', data)



def modificar(request, id):
    producto = Producto.objects.get(id=id)
    data= {
        'form' : ProductoForm(instance = producto),
    }

    if request.method == 'POST' : 
        formulario = ProductoForm(data=request.POST, instance=producto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "Modificado Correctamente"
        data['form'] = ProductoForm(instance=Producto.objects.get(id=id))

    return render(request, 'PaginaWeb/modificar.html', data)
