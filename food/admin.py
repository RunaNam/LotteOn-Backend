from django.contrib import admin

# Register your models here.
from food.models import Ingredients, Recipe, Warn, Feature, CrossReaction, Allergies

admin.site.register(Recipe)
admin.site.register(Feature)
admin.site.register(Warn)
admin.site.register(CrossReaction)
admin.site.register(Allergies)


@admin.register(Ingredients)
class IngredientsAdmin(admin.ModelAdmin):
    list_display = ['name']

#

