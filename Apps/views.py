from django.shortcuts import render


def home(request):
    return render(request, "core/home.html")

def sample(request):
    return render(request, "core/sample.html")

def bienvenido(request):
    return render(request, "core/bienvenido.html")

def desarrollo(request):
    return render(request, "core/desarrollo.html")

def diseño(request):
    return render(request, "core/diseño.html")