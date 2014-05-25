from django.db import models
from django.utils.translation import ugettext_lazy as _
from mezzanine.pages.models import Page, RichText

class TreePage(Page, RichText):
    """
    A tree page
    """
    add_toc = models.BooleanField(_("Add TOC"), default=False,
                                  help_text=_("Include a list of child links"))

    class Meta:
        verbose_name = _("Tree Page")
        verbose_name_plural = _("Tree Pages")

# Create your models here.
