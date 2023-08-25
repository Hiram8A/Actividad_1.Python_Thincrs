from django.http import HttpResponse
from django.views import View
from django.shortcuts import render, HttpResponse, redirect

from django.contrib.auth import authenticate, login
from django.contrib import messages 
from django.contrib.auth import logout

def custom_logout(request):
    logout(request)
    return redirect('/productos/home')

# Accedemos al metodo POST para hacer el request del Login
def custom_login(request):
    template_name = 'login.html'
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username, password=password)

        if user is not None:
            login(request, user)
            print('-------------> Si entro al login')
            return redirect('/productos/home')
        
        else:
            print('-------------> No entró al login')
            messages.error(request, 'Credenciales Erróneas')
            
            
    return render(request, template_name)