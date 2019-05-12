from django.shortcuts import render, redirect
from recipe.models import *
from .forms import RecipeSubmissionForm, VoteSubmissionForm
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
        elif 'vote' in request.POST:
            form = VoteSubmissionForm(request.POST) #forma veri gelmiyor
            if form.is_valid():
                recipe_vote = recipe.recipe_vote
                recipe_vote_count = recipe.recipe_vote_count
                recipe_vote = (int(recipe_vote) * int(recipe_vote_count) + form.cleaned_data['vote']) / (int(recipe_vote_count) + 1)
                recipe_vote_count = int(recipe_vote_count) + 1
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
