from django.db import models
from mezzanine.pages.models import Page, RichTextPage
from django.utils.translation import ugettext_lazy as _

from mezzanine.core.models import RichText
from mezzanine.core.fields import RichTextField

# The members of Page will be inherited by the Author model, such
# as title, slug, etc. For authors we can use the title field to
# store the author's name. For our model definition, we just add
# any extra fields that aren't part of the Page model, in this
# case, date of birth.

class Author(Page,RichText):
    dob = models.DateField("Date of birth") 

    class Meta:
        verbose_name = _("Author")
        verbose_name_plural = _("Authors")



class Book(Page,RichText):
    authors = models.ManyToManyField("Author",blank=True, related_name="books")
    publisher = models.CharField(max_length=200,blank=True)
    cover = models.ImageField(upload_to="books",blank=True)

    class Meta:
        verbose_name = _("Book")
        verbose_name_plural = _("Books")

class Excerpt(Page,RichText):
    book = models.ForeignKey("Book",blank=True, related_name="excerpts")

    class Meta:
        verbose_name = _("Excerpt")
        verbose_name_plural = _("Excerpts")
    

