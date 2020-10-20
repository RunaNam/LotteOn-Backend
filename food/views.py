from django.shortcuts import render
from .models import Ingredients
from rest_framework import generics
from .serializers import IngredientsSerializer


class IngredientsList(generics.ListCreateAPIView):
    queryset = Ingredients.objects.all()
    serializer_class = IngredientsSerializer
