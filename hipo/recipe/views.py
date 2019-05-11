from django.shortcuts import render
from recipe.models import *

def index(request):
    recipes = Recipe.objects.all()
    return render(request, 'index.html', {
        'title': 'Home',
        'recipes': recipes,
    })
