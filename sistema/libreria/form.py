from django import forms 
from .models import Book

class LibroForm(forms.ModelForm):
    class Meta: 
        model = Book 
        fields = '__all__'