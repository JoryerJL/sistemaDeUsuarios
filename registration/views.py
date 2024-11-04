from lib2to3.fixes.fix_input import context

from django.contrib.auth import authenticate, login
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

def index(request):
    return render(request, 'registration/index.html')