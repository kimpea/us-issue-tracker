from django.test import TestCase
from .forms import RequestFeatureForm, FeatureCommentForm

class TestRequestFeatureForm(TestCase):

    def test_feature_has_name_and_description(self):
        form = RequestFeatureForm(
            {'name': 'Feature Name',
            'description': 'Feature Description'})
        self.assertTrue(form.is_valid())
        
    def test_feature_without_name_or_description(self):
        form = RequestFeatureForm({
            'name': 'Feature Name',
            'description': ''
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['description'], ['This field is required.'])
        
class TestFeatureCommentForm(TestCase):
    
    def test_feature_comment_form(self):
        form = FeatureCommentForm({'comment': 'This is a comment'})
        self.assertTrue(form.is_valid())