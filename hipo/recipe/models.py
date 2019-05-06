from django.db import models
from django.conf import settings
from django.utils import timezone

RECIPE_STAGE_CHOICES = (
    ('easy', 'Easy'),
    ('medium', 'Medium'),
    ('hard', 'Hard'),
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
    recipe_name = models.CharField(max_length=30)
    recipe_content = models.CharField(max_length=255)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.recipe_name
