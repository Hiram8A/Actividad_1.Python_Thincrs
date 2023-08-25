from django.http import HttpResponse, JsonResponse
from django.views import View
from django.shortcuts import render, redirect, get_object_or_404

from .models import Productos 
from .forms import ProductoForm


def index(request):

    return HttpResponse("Hola mundo")

class Inicio(View):
    template_name = 'productos.html'

    def post(self,request):

        return render(request,self.template_name)


    def get(self,request):
        productos = Productos.objects.all()

        return render(request,self.template_name,{'productos':productos})
    
class Formulario(View):
    template_name = 'formulario.html'
    
    def post(self,request):
        form = ProductoForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('home')
        
        #else:
        #    JsonResponse("Se ha presentado un error")
            
        return render(request,self.template_name,{'form': form})

    def get(self,request):

        productos = Productos.objects.all()
        form = ProductoForm()

        return render(request,self.template_name,{'form':form})

def insertar_producto(request):
    nuevo_producto = Productos(
        nombre = "Mazapan",
        descripcion = "Dulce de cacahuate",
        precio = 5,
        estatus = "True" 
    )
    nuevo_producto.save()

    return HttpResponse("Producto Insertado Correctamente")

class Eliminar_Productos(View):
    def post(self, request, producto_id):
        producto = get_object_or_404(Productos, pk=producto_id)
        producto.delete()
        return redirect('home')