from django.urls import path

from . import views

urlpatterns = [
    path('', views.IngredientsList.as_view()),

]