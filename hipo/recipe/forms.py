from django import forms
from multiselectfield import MultiSelectField


RECIPE_STAGE_CHOICES = (
    ('easy', 'Easy'),
    ('medium', 'Medium'),
    ('hard', 'Hard'),
)

RECIPE_INGREDIENTS_CHOICE = (
    ('tomato', 'Tomato'),
    ('milk', 'Milk'),
    ('oil', 'Oil'),
    ('egg', 'Egg'),
    ('cheese', 'Cheese'),
    ('chicken', 'Chicken'),
)

class RecipeSubmissionForm(forms.Form):
    recipe_name = forms.CharField(
        max_length=30,
        label='Recipe Name',
        required=True,
    )
    recipe_image = forms.ImageField()
    recipe_content = forms.CharField(
        widget=forms.Textarea
    )
    recipe_stage = forms.ChoiceField(
        choices=RECIPE_STAGE_CHOICES,
        required=True,
        label='Recipe Stage',
        widget=forms.Select,
    )
    recipe_ingredients = MultiSelectField(
        choices=RECIPE_INGREDIENTS_CHOICE
    )
