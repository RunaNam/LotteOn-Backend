from django.contrib import admin
from checklist.models import Allergy, Etc


@admin.register(Allergy)
class AllergyAdmin(admin.ModelAdmin):
    list_display = ['id', 'content']

@admin.register(Etc)
class EtcAdmin(admin.ModelAdmin):
    list_display = ['id', 'content']