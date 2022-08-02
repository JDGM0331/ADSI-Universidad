from django.db import models

# Create your models here.

class Book(models.Model): 
    id = models.AutoField(primary_key=True) # autoincremental number field
    title = models.CharField(max_length=100, verbose_name="Description") # limited text field
    image = models.ImageField(upload_to='images/', verbose_name="Description", null=True) # image fiel 
    description = models.TextField(verbose_name="Description", null=True)