from django.shortcuts import render

# my_app/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)
from .models import Recipe, Comment
from .forms import RecipeForm, CommentForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect


class RecipeList(ListView):
    """Display a list (index) of all recipes."""
    model = Recipe
    template_name = 'my_app/recipe_list.html'
    context_object_name = 'recipes'
    paginate_by = 6


class RecipeDetail(DetailView):
    """Show details of a single recipe, including an add‐comment form."""
    model = Recipe
    template_name = 'my_app/recipe_detail.html'
    context_object_name = 'recipe'

    def get_context_data(self, **kwargs):
        """
        Add the CommentForm and existing comments to the context so they can be
        displayed on the detail page.
        """
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        context['comments'] = self.object.comments.order_by('-created_at')
        return context


class RecipeCreate(LoginRequiredMixin, CreateView):
    """Allow a logged‐in user to create a new recipe."""
    model = Recipe
    form_class = RecipeForm
    template_name = 'my_app/recipe_form.html'


    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class RecipeUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """Allow the recipe’s owner to edit the recipe."""
    model = Recipe
    form_class = RecipeForm
    template_name = 'my_app/recipe_form.html'

    def test_func(self):
        recipe = self.get_object()
        return recipe.user == self.request.user


class RecipeDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """Allow the recipe’s owner to delete it."""
    model = Recipe
    template_name = 'my_app/recipe_confirm_delete.html'
    success_url = reverse_lazy('my_app:recipe_index')

    def test_func(self):
        recipe = self.get_object()
        return recipe.user == self.request.user


@login_required
def add_comment(request, recipe_id):
    """Handle posting a new comment on a recipe detail page."""
    recipe = get_object_or_404(Recipe, id=recipe_id)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.recipe = recipe
            comment.save()
            return redirect('my_app:recipe_detail', pk=recipe.id)
    else:
        form = CommentForm()

    return render(request, 'my_app/comment_form.html', {
        'form': form,
        'recipe': recipe
    })


class CommentUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """Allow a comment’s author to edit their comment."""
    model = Comment
    form_class = CommentForm
    template_name = 'my_app/comment_form.html'

    def test_func(self):
        comment = self.get_object()
        return comment.user == self.request.user

    def get_success_url(self):

        return self.object.recipe.get_absolute_url()


class CommentDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """Allow a comment’s author to delete their comment."""
    model = Comment
    template_name = 'my_app/comment_confirm_delete.html'

    def test_func(self):
        comment = self.get_object()
        return comment.user == self.request.user

    def get_success_url(self):
        return self.object.recipe.get_absolute_url()




def signup(request):
    """
    Display a registration form and create a new user if the form is valid.
    After creating the user, immediately log them in and redirect to the homepage.
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()          
            login(request, user)        
            return redirect('my_app:recipe_index')
    else:
        form = UserCreationForm()

    return render(request, 'registration/signup.html', {'form': form})