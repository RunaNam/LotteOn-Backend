from django.db import models


class Warn(models.Model):
    content = models.CharField(max_length=100)

    def __str__(self):
        return self.content


class Feature(models.Model):
    content = models.CharField(max_length=100)

    def __str__(self):
        return self.content


class CrossReaction(models.Model):
    content = models.CharField(max_length=100)

    def __str__(self):
        return self.content


class Allergies(models.Model):
    content = models.CharField(max_length=100)

    def __str__(self):
        return self.content


class RecipeIng(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Seasoning(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Direction(models.Model):
    order = models.CharField(max_length=100)
    image = models.ImageField(blank=True)

    def __str__(self):
        return self.order


class RelatedReceipe(models.Model):
    content = models.CharField(max_length=100)

    def __str__(self):
        return self.content


class Recipe(models.Model):
    name = models.CharField(max_length=100)
    division = models.CharField(max_length=20)
    recipeIng = models.ManyToManyField(RecipeIng, blank=True)
    seasoning = models.ManyToManyField(Seasoning, blank=True)
    directions = models.ManyToManyField(Direction, blank=True)
    image = models.ImageField(blank=True)
    time = models.CharField(max_length=30)
    serving = models.CharField(max_length=30)
    allergies = models.ManyToManyField(Allergies, blank=True)
    feature = models.ManyToManyField(Feature, blank=True)

    def __str__(self):
        return self.name


class Ingredients(models.Model):
    division = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    barcodeNumber = models.IntegerField()
    relatedRecipes = models.ManyToManyField(RelatedReceipe, blank=True)
    brand = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    warnings = models.ManyToManyField(Warn, blank=True)
    image = models.ImageField(blank=True)
    feature = models.ManyToManyField(Feature, blank=True)
    crossReaction = models.ManyToManyField(CrossReaction, blank=True)
    allergies = models.ManyToManyField(Allergies, blank=True)
