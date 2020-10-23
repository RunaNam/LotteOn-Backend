from django.contrib import admin

# Register your models here.
from food.models import *

admin.site.register(Recipe)
admin.site.register(Feature)
admin.site.register(Warn)
admin.site.register(CrossReaction)

admin.site.register(Allergies)
admin.site.register(RelatedReceipe)
admin.site.register(RecipeIng)
admin.site.register(Seasoning)
admin.site.register(Direction)


@admin.register(Ingredients)
class IngredientsAdmin(admin.ModelAdmin):
    list_display = ['name']

#

