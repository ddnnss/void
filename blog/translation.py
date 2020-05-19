from modeltranslation.translator import register, TranslationOptions
from .models import *


@register(ArticleType)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(Article)
class SubCategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'description',)


