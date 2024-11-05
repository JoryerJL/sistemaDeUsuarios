from lib2to3.fixes.fix_input import context

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
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
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        if email and password:
            try:
                usuario = User.objects.create_user(username=email, email=email, password=password)
                login(request, usuario)
                context.update({"message": f'Usuario {usuario.username} creado exitosamente'})
            except Exception as e:
                context.update({"message": f'Usuario {email} ya existe, inicie sesión'})
    return render(request, 'registration/custom_register.html', context)

def logout_view(request):
    logout(request)
    return redirect('registration:index')
def index(request):
    return render(request, 'registration/index.html')