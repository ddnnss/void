from django.contrib import admin
from .models import *



class CallbackAdmin(admin.ModelAdmin):
    list_display = ['name', 'user_phone', 'is_done', 'created_at' ]
    search_fields = ('user_phone',)
    list_filter = ('created_at', 'is_done')
    class Meta:
        model = Callback

admin.site.register(Callback,CallbackAdmin)
