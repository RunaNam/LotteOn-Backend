from django.contrib import admin
from checklist.models import Allergy

@admin.register(Allergy)
class AllergyAdmin(admin.ModelAdmin):
    list_display = ['id', 'content']