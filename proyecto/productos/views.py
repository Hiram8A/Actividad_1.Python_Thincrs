from django.http import HttpResponse, JsonResponse
from django.views import View
from django.shortcuts import render, redirect

from .models import Productos 
from .forms import ProductoForm


def index(request):

    return HttpResponse("Hola mundo")

class Inicio(View):
    template_name = 'productos.html'

    def post(self,request):
        form = ProductoForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('home')
        
        #else:
        #    JsonResponse("Se ha presentado un error")
        
        return render(request,self.template_name,{'form': form})

    def get(self,request):
        '''Esta es mi clase GET'''
        productos = Productos.objects.all()
        form = ProductoForm()
        #print('Ha iniciado GET --------------------------')

        return render(request,self.template_name,{'form': form,'productos':productos})
    
def insertar_producto(request):
    nuevo_producto = Productos(
        nombre = "Mazapan",
        descripcion = "Dulce de cacahuate",
        precio = 5,
        estatus = "True"
    )
    nuevo_producto.save()

    return HttpResponse("Producto Insertado Correctamente")

