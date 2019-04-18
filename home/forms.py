from django import forms
from .models import Question

class FAQForm(forms.ModelForm):
    class Meta: 
        model = Question
        fields = ('question', 'description')