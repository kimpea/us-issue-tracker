from django import forms
from .models import Feature, FeatureComments

class RequestFeatureForm(forms.ModelForm):
    class Meta: 
        model = Feature
        fields = ('name', 'description')
        
class FeatureCommentForm(forms.ModelForm):
    comment = forms.CharField(widget=forms.Textarea(
        attrs={'rows': '4', 'cols': '5'}))

    class Meta:
        model = FeatureComments
        fields = ['comment']