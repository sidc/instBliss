from django.contrib import admin
from mezzanine.pages.admin import PageAdmin
from .models import Recipe, RecipeGallery

admin.site.register(Recipe, PageAdmin)
admin.site.register(RecipeGallery, PageAdmin)

# Register your models here.
