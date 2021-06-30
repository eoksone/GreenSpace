from django.db import models

# Create your models here.


class Categoria(models.Model): 
    categoria = models.CharField(max_length=200, null=False)
    def __str__(self):
        return self.categoria


class Producto(models.Model):
    nombre = models.CharField(max_length=200, null=False,verbose_name='Nombre producto')
    marca = models.CharField(max_length=100, null=False,verbose_name='Marca producto')
    formato =models.CharField (max_length=20,null=True,blank=True,verbose_name='Formato')
    codigo = models.CharField(max_length=50, null=False,verbose_name='Codigo del producto')
    valor = models.IntegerField(null=False,verbose_name='Precio producto')
    imagen = models.ImageField(upload_to="instrumentos", null=True)
    categoriapro= models.ForeignKey(Categoria,on_delete=models.CASCADE,verbose_name='Categoria producto')
    
    def __str__(self):
        return self.nombre

