from lib2to3.fixes.fix_input import context

from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

# Create your views here.
def custom_login(request):
    context = {}
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            print("Login exitoso")
            return redirect('registration:index')
        else:
            context.update({"error": "Usuario o contraseña incorrectos"})
    return render(request, 'registration/custom_login.html', context)

def custom_register(request):
    context = {}
    return render(request, 'registration/custom_register.html', context)

def logout_view(request):
    logout(request)
    return redirect('registration:index')
def index(request):
    return render(request, 'registration/index.html')