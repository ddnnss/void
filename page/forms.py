from django.forms import ModelForm

from .models import *



class CallbackOrderForm(ModelForm):
    class Meta:
        model = Callback
        fields = (
            'name',
            'user_phone',
        )
