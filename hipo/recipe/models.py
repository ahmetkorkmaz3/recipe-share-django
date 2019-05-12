from django.db import models
from django.conf import settings
from django.utils import timezone
from multiselectfield import MultiSelectField

RECIPE_STAGE_CHOICES = (
    ('easy', 'Easy'),
    ('medium', 'Medium'),
    ('hard', 'Hard'),
)

RECIPE_VOTE_CHOICES = (
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

RECIPE_INGREDIENTS_CHOICE = (
    ('tomato', 'Tomato'),
    ('milk', 'Milk'),
    ('oil', 'Oil'),
    ('egg', 'Egg'),
    ('cheese', 'Cheese'),
    ('chicken', 'Chicken'),
)

class Recipe(models.Model):
    """
    """
    recipe_user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        on_delete=models.CASCADE,
    )
    recipe_stage = models.CharField(
        max_length=30,
        choices=RECIPE_STAGE_CHOICES,
    )
    recipe_image = models.ImageField(
        blank=True,
        null=True,
    )
    recipe_name = models.CharField(max_length=30)
    recipe_ingredients = MultiSelectField(choices=RECIPE_INGREDIENTS_CHOICE, blank=True)
    recipe_content = models.CharField(max_length=2000)
    recipe_vote = models.CharField(
        max_length=30,
        choices=RECIPE_VOTE_CHOICES,
        default='0',
    )
    recipe_vote_count = models.CharField(max_length=30, default='0')
    recipe_like = models.CharField(max_length=30, default='0')
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.recipe_name
