from django.db import models

# Create your models here.

class Book(models.Model): 
    id = models.AutoField(primary_key=True) # autoincremental number field
    title = models.CharField(max_length=100, verbose_name="Description") # limited text field
    image = models.ImageField(upload_to='images/', verbose_name="Description", null=True) # image fiel 
    description = models.TextField(verbose_name="Description", null=True)

    def __str__(self) -> str: # Muestra una descripción personalizada el momento que se consulten los registros del libro
        fila = "Título: " + self.title + " - " + "Descripción " + self.description
        return fila 

    # Al momento de eliminar un libro esta función permite eliminar 
    # la imagen asociada al libro y que se encuentra dentro del proyecto. 
    def delete(self, using=None, keep_parents=False): 
        self.image.storage.delete(self.image.name)
        super().delete()