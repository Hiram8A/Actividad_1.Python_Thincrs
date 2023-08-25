from django.http import HttpResponse, JsonResponse
from django.views import View
from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.db.models import Sum, Max, Avg

from .models import Productos 
from .forms import ProductoForm


def index(request):

    return HttpResponse("Hola mundo")

class Inicio(View):
    template_name = 'productos.html'

    def post(self,request):

        return render(request,self.template_name)
    @method_decorator(login_required)


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
    
def estadisticas_productos(request):
    # Obtener el Numero Total de Productos disponibles
    total_productos = Productos.objects.aggregate(total_productos=Sum('estatus'))['total_productos'] 

    # Obtener el Año Más Reciente de Fecha de Registro
    max_fecha_registro = Productos.objects.aggregate(max_fecha_registro=Max('fecha_registro'))['max_fecha_registro'] 

    # Obtener el Promedio de los Precios de Productos
    promedio_precio = Productos.objects.aggregate(promedio_precio=Avg('precio'))['promedio_precio']

    return render(request, 'estadisticas/estadisticas_productos.html', {
        'total_productos': total_productos,
        'max_fecha_registro': max_fecha_registro,
        'promedio_precio': promedio_precio,
    })