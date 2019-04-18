from django.test import TestCase
from .models import Feature, FeatureComments
from django.contrib.auth.models import User

# Create your tests here.
class TestFeature(TestCase):
    """
    Here we'll define the tests that we'll run against our
    Feature model
    """

    def test_str(self):
        test_name = Feature(name='A feature')
        self.assertEqual(str(test_name), 'A feature')