from django.urls import path
from . import views

app_name = 'my_app'

urlpatterns = [
    # --- Recipe CRUD URLs ---
   
    path('', views.RecipeList.as_view(), name='recipe_index'),
    path('recipes/<int:pk>/', views.RecipeDetail.as_view(), name='recipe_detail'),
    path('recipes/create/', views.RecipeCreate.as_view(), name='recipe_create'),
    path('recipes/<int:pk>/update/', views.RecipeUpdate.as_view(), name='recipe_update'),
    path('recipes/<int:pk>/delete/', views.RecipeDelete.as_view(), name='recipe_delete'),

    # --- Comment URLs ---

    path(
        'recipes/<int:recipe_id>/comments/add/',
        views.add_comment,
        name='comment_add'
    ),

    path('comments/<int:pk>/update/', views.CommentUpdate.as_view(), name='comment_update'),
    path('comments/<int:pk>/delete/', views.CommentDelete.as_view(), name='comment_delete'),
]
