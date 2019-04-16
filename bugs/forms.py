from django import forms
from .models import Bug

class ReportBugForm(forms.ModelForm):
    class Meta: 
        model = Bug
        fields = ('name', 'description')
