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
            recipe = Recipe.objects.create(
                recipe_user=request.user,
                recipe_stage=form.cleaned_data['recipe_stage'],
                recipe_name=form.cleaned_data['recipe_name'],
                recipe_content=form.cleaned_data['recipe_content'],
                recipe_ingredients=form.cleaned_data['recipe_ingredients'],
                recipe_image=form.cleaned_data['recipe_image']
            )
            recipe.save()
            return redirect('index')
    else:
        return render(request, 'share.html', {'form': form})
