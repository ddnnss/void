from modeltranslation.translator import register, TranslationOptions
from .models import *


@register(Partner)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name','description')


@register(Unit)
class SubCategoryTranslationOptions(TranslationOptions):
    fields = ('name', )


