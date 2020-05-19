from django.contrib import admin
from .models import *

class UnitInline (admin.TabularInline):
    model = Unit.price_item.through
    # readonly_fields = ('image_tag', )
    extra = 0

class PartnerAdmin(admin.ModelAdmin):
    list_display = ['name',]
    #list_display = [field.name for field in Item._meta.fields]
    inlines = [UnitInline]

    class Meta:
        model = Partner




admin.site.register(Partner,PartnerAdmin)
admin.site.register(Unit)

