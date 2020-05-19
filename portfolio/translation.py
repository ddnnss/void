from modeltranslation.translator import register, TranslationOptions
from .models import *


@register(PortfolioItem)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name','description')





