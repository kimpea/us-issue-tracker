from django import forms
from .models import Bug, BugComments

class ReportBugForm(forms.ModelForm):
    class Meta: 
        model = Bug
        fields = ('name', 'description')

class BugCommentForm(forms.ModelForm):
    comment = forms.CharField(widget=forms.Textarea(
        attrs={'rows': '4', 'cols': '5'}))

    class Meta:
        model = BugComments
        fields = ['comment']