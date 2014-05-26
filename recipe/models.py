from django.db import models

from django.utils.translation import ugettext_lazy as _
# Create your models here.
from django.db import models
from mezzanine.pages.models import Page, RichTextPage

from mezzanine.core.models import RichText
from mezzanine.core.fields import RichTextField



class Recipe(Page,RichText):
    image = models.ImageField(upload_to="recipes",blank=True)
    
    class Meta:
        verbose_name = _("Recipe")
        verbose_name_plural = _("Recipes")


class RecipeGallery(Page, RichText):
    """
    A tree page
    """
    add_toc = models.BooleanField(_("Add TOC"), default=True,help_text=_("Include a list of child links"))

    class Meta:
        verbose_name = _("Recipe Gallery")
        verbose_name_plural = _("Recipe Galeries")

# Create your models here.
