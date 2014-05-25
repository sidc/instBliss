from django.contrib import admin
from mezzanine.pages.admin import PageAdmin
from .models import TreePage

admin.site.register(TreePage, PageAdmin)

# Register your models here.
