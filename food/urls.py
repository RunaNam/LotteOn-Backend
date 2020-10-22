from django.urls import path

from . import views

urlpatterns = [
    path('ingredient/', views.IngredientsList.as_view()),
    path('receipe/', views.RecipeList.as_view()),
]