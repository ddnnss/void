from django.contrib import admin
from .models import *

class ArticleInline (admin.TabularInline):
    model = Article
    # readonly_fields = ('image_tag', )
    extra = 0

class ArticleTypeAdmin(admin.ModelAdmin):
    list_display = ['name',]
    #list_display = [field.name for field in Item._meta.fields]
    inlines = [ArticleInline]

    class Meta:
        model = ArticleType


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['name','is_active' ]
    autocomplete_lookup_fields = {
        'name': ['name'],

    }

    class Meta:
        model = Article


admin.site.register(ArticleType,ArticleTypeAdmin)
admin.site.register(Article,ArticleAdmin)
