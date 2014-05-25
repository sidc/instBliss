from copy import deepcopy
from django.contrib import admin
from mezzanine.core.admin import StackedDynamicInlineAdmin, TabularDynamicInlineAdmin
from mezzanine.pages.admin import PageAdmin
from .models import Excerpt, Author, Book

excerpt_extra_fieldsets = ((None, {"fields": ("book","content")}),)
excerpt_fieldsets = deepcopy(PageAdmin.fieldsets)
excerpt_fieldsets[0][1]["fields"].insert(1, "book")

class ExcerptAdmin(PageAdmin):
    fieldsets = excerpt_fieldsets

admin.site.register(Author, PageAdmin)
admin.site.register(Book, PageAdmin)
admin.site.register(Excerpt, ExcerptAdmin)

