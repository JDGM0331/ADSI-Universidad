from operator import imod
from django.shortcuts import render
from django.http import HttpResponse
from. models import Book
from .form import LibroForm

# Create your views here.

def inicio(request):  # Mostrar un título como vista
   # return HttpResponse("<h1>Proyecto Django Universidad.</h1>") 
   return render(request, 'pages/index.html')

def nosotros(request): # Mostrar una vista html 
    return render(request, 'pages/nosotros.html')

def index(request):
   books = Book.objects.all()
   return render(request, 'books/index.html', {'books' : books})

def form(request):
   return render(request, 'books/form.html')

def add(request):
   formulario = LibroForm(request.POST or None)
   return render(request, 'books/add.html', {'formulario' : formulario})

def edit(request):
   return render(request, 'books/edit.html')