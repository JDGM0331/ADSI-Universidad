from importlib.resources import path
from unicodedata import name
import django


from django.urls import URLPattern, path
from.import views 

urlpatterns = [
    path('',views.inicio, name='inicio'),
    path('nosotros',views.nosotros, name='nosotros'),

    # Rutas de Books
    path('index',views.index, name='index'),
    path('form',views.form, name='form'),
    path('add',views.add, name='add'),
    path('edit',views.edit, name='edit'),
]