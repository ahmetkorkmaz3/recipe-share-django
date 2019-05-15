from django.shortcuts import render, redirect
from recipe.models import *
from .forms import RecipeSubmissionForm, VoteSubmissionForm
from django.urls import reverse
from django.db.models import Count
import math


def index(request):
    recipes = Recipe.objects.all().order_by('-created_date')
    #Search
    query = request.GET.get('search')
    if query:
        recipes = Recipe.objects.all().filter(recipe_name__icontains=query)
        if not recipes:
            recipes = Recipe.objects.all().filter(recipe_ingredients__contains=query)
    #top ingredients
    ingredients = Recipe.objects.all().values('recipe_ingredients').annotate(total=Count('recipe_ingredients')).order_by('recipe_ingredients')
    if ingredients:
        max = ingredients[0].get('total')
        top_ingredients = ingredients[0]
        for count in ingredients:
            if max < count.get('total'):
                max = count.get('total')
                top_ingredients = count

        top_ingredients = top_ingredients['recipe_ingredients']
    else:
        top_ingredients = 0
        max = 0
    return render(request, 'index.html', {
        'title': 'Home',
        'recipes': recipes,
        'top_ingredients': top_ingredients,
        'top_ingredients_count': max,
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

def recipe_detail(request, recipe_name):
    recipe = Recipe.objects.get(recipe_name=recipe_name)
    form = VoteSubmissionForm()
    if request.method == 'POST':
        recipe = Recipe.objects.get(recipe_name=recipe_name)
        if 'Like' in request.POST:
            recipe_like = recipe.recipe_like
            recipe_like = int(recipe_like) + 1
            recipe = Recipe.objects.filter(recipe_name=recipe_name).update(recipe_like=recipe_like)
            recipe = Recipe.objects.get(recipe_name=recipe_name)
            return render(request, 'detail.html', {
                'recipe': recipe,
                'form': form,
            })
        elif 'rate' in request.POST:
            form = VoteSubmissionForm(request.POST)
            if form.is_valid():
                vote_value = form.cleaned_data['vote']
                vote_value = int(vote_value)
                recipe_vote = recipe.recipe_vote
                recipe_vote_count = recipe.recipe_vote_count
                recipe_vote = (float(recipe_vote) * float(recipe_vote_count) + vote_value) / (float(recipe_vote_count) + 1)
                recipe_vote_count = float(recipe_vote_count) + 1
                recipe = Recipe.objects.filter(recipe_name=recipe_name).update(recipe_vote=recipe_vote, recipe_vote_count=recipe_vote_count)
                recipe = Recipe.objects.get(recipe_name=recipe_name)
                return render(request, 'detail.html', {
                    'recipe': recipe,
                    'form': form,
                })
            else:
                return redirect('index')

    return render(request, 'detail.html', {
        'recipe': recipe,
        'form': form,
    })
