from django.test import TestCase
from .models import Bug
from django.contrib.auth.models import User

# Create your tests here.
class TestBug(TestCase):
    """
    Here we'll define the tests that we'll run against our
    Bug model
    """

    def test_str(self):
        test_name = Bug(name='A bug')
        self.assertEqual(str(test_name), 'A bug')
