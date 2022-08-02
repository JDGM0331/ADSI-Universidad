from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def inicio(request):  # Mostrar un título como vista
   # return HttpResponse("<h1>Proyecto Django Universidad.</h1>") 
   return render(request, 'pages/index.html')

def nosotros(request): # Mostrar una vista html 
    return render(request, 'pages/nosotros.html')

def index(request):
   return render(request, 'books/index.html')

def form(request):
   return render(request, 'books/form.html')

def add(request):
   return render(request, 'books/add.html')

def edit(request):
   return render(request, 'books/edit.html')