# my_app/models.py

from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Optional: define the choices for skill level
SKILL_CHOICES = [
    ('Beginner', 'Beginner'),
    ('Intermediate', 'Intermediate'),
    ('Advanced', 'Advanced'),
]

class Recipe(models.Model):
    cuisine = models.CharField(
        max_length=100,
        help_text="e.g. Italian, Mexican, Thai..."
    )
    cooking_time = models.IntegerField(
        help_text="Cooking time in minutes"
    )
    skill_level = models.CharField(
        max_length=20,
        choices=SKILL_CHOICES
    )
    # Link each recipe to the User who created it
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='recipes'
    )

    def __str__(self):
        return f"{self.cuisine} ({self.skill_level})"

    def get_absolute_url(self):
        # After creating/updating a Recipe, redirect to its detail page
        return reverse('my_app:recipe_detail', args=[self.id])


class Comment(models.Model):
    text = models.TextField()
    # Each comment belongs to exactly one Recipe
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    # And each comment is authored by a User
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.text[:20]}… by {self.user.username}"

    def get_absolute_url(self):
        # After saving/updating a comment, go back to the Recipe’s detail page
        return reverse('my_app:recipe_detail', args=[self.recipe.id])
