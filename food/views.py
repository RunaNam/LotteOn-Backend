from django.shortcuts import render
from .models import Ingredients, Recipe
from rest_framework import generics
from .serializers import IngredientsSerializer, RecipeSerializer


class IngredientsList(generics.ListCreateAPIView):
    queryset = Ingredients.objects.all()
    serializer_class = IngredientsSerializer


class RecipeList(generics.ListCreateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
