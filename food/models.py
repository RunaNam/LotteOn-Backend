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


class Recipe(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Ingredients(models.Model):
    division = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    barcodeNumber = models.IntegerField()
    relatedRecipes = models.ManyToManyField(Recipe, blank=True)
    brand = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    warnings = models.ManyToManyField(Warn, blank=True)
    image = models.ImageField()
    feature = models.ManyToManyField(Feature, blank=True)
    crossReaction = models.ManyToManyField(CrossReaction, blank=True)
    allergies = models.ManyToManyField(Allergies, blank=True)

# class RecipeIng(models.Model):
#     name = models.CharField(max_length=100)
#     quantity = models.IntegerField()
#
#     def __str__(self):
#         return self.name
#
#
# class Seasoning(models.Model):
#     name = models.CharField(max_length=100)
#     quantity = models.IntegerField()
#
#     def __str__(self):
#         return self.name

# recipe 내용인데 아직.. 다 못만듬
#     division = models.CharField(max_length=20)
#     ingredients = models.ManyToManyField(RecipeIng, blank=True)
#     seasoning = models.ManyToManyField(Seasoning, blank=True)
#     directions = models.ManyToManyField(Warn, blank=True)
#     image = models.ImageField()
#     feature = models.ManyToManyField(Feature, blank=True)
#     crossReaction = models.ManyToManyField(CrossReaction, blank=True)
#     allergies = models.ManyToManyField(Allergies, blank=True)
