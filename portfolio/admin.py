from django.contrib import admin
from .models import *


class ImagesInline (admin.TabularInline):
    model = PortfolioItemImage
    # readonly_fields = ('image_tag', )
    extra = 0

class PortfolioItemAdmin(admin.ModelAdmin):
    list_display = ['name','image','description',]
    #list_display = [field.name for field in Item._meta.fields]
    inlines = [ImagesInline]

    class Meta:
        model = PortfolioItem

admin.site.register(PortfolioItem,PortfolioItemAdmin)
admin.site.register(PortfolioItemImage)
