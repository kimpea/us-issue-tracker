from django.test import TestCase
from .forms import RequestFeatureForm, FeatureCommentForm

class TestRequestFeatureForm(TestCase):

    def test_feature_has_name_and_description(self):
        form = RequestFeatureForm(
            {'name': 'Feature Name',
            'description': 'Feature Description'})
        self.assertTrue(form.is_valid())