from django import forms
from .models import Feature

class RequestFeatureForm(forms.ModelForm):
    class Meta: 
        model = Feature
        fields = ('name', 'description')