from django import forms
from multiselectfield import MultiSelectField
from .models import Recipe

VOTE_CHOICES = (
    ('0', '0'),
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
    ('7', '7'),
    ('8', '8'),
    ('9', '9'),
    ('10', '10')
)

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
        widgets = {
            'recipe_content': forms.Textarea(attrs={'cols':80, 'rows': 20})
        }

class VoteSubmissionForm(forms.ModelForm):
    class Meta:
        model = Recipe
        field = ['recipe_vote_count']
