from django.shortcuts import render, redirect
from recipe.models import *
from .forms import RecipeSubmissionForm
from django.urls import reverse

def index(request):
    recipes = Recipe.objects.all()
    return render(request, 'index.html', {
        'title': 'Home',
        'recipes': recipes,
    })

def share(request):
    form = RecipeSubmissionForm()
    if request.method == 'POST':
        form = RecipeSubmissionForm(request.POST, request.FILES)
        if form.is_valid():
            # Veritabanına ekleme işlemi yapılacak
            return render(request, 'index.html')
    else:
        return render(request, 'share.html', {'form': form})
