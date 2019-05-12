from django import forms
from multiselectfield import MultiSelectField
from .models import Recipe


class RecipeSubmissionForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = [
            'recipe_name',
            'recipe_image',
            'recipe_content',
            'recipe_stage',
            'recipe_ingredients'
        ]
