from django.test import TestCase
from .forms import UserLoginForm, UserRegistrationForm
from django.contrib.auth.models import User

# Create your tests here.
class TestForms(TestCase):
    
    # Registration Form Tests
    def test_if_user_can_be_registered(self):
        form = UserRegistrationForm(
            {
                'email': 'test@test.com',
                'username': 'Testing',
                'password1': 'test123',
                'password2': 'test123',
            }
        )
        self.assertTrue(form.is_valid())
        
    def test_if_user_requires_email(self):
        form = UserRegistrationForm(
            {
                'email': '', 
                'username': 'Testing',
                'password1': 'test123',
                'password2': 'test123',
            }
        )
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['email'], [u'This field is required.'])