from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def home(request):
    return render(request, 'home.html')

def atualizacoes(request):
    return render(request, 'atualizacoes.html')

def comentarios(request):
    return render(request, 'comentarios.html')

def imagens(request):
    return render(request, 'imagens.html')