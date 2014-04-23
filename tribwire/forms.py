from django import forms
from .models import Link

class PostModelForm(forms.ModelForm):
    class Meta:
        model = Link
       