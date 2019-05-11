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
        form = RecipeSubmissionForm(request.POST)
        if form.is_valid(): # form is valid olmuyor
            return redirect(reverse('index.html', args='1'))
        else:
            print("else")
            return False
    else:
        return render(request, 'share.html', {'form': form})
