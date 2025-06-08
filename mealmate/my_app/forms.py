from django import forms
from .models import Recipe, Comment

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'cuisine', 'cooking_time', 'skill_level', 'external_link']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'e.g. Spaghetti Carbonara'}),
            'cuisine': forms.TextInput(attrs={'placeholder': 'e.g. Italian, Mexican…'}),
            'cooking_time': forms.NumberInput(attrs={'min': 1}),
            'skill_level': forms.Select(),
            'external_link': forms.URLInput(attrs={'placeholder': 'https://…'}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Write your comment here…'}),
        }
