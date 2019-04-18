from django.test import TestCase
from .forms import MakePaymentForm, OrderForm

class TestMakePaymentForm(TestCase):
    
    def test_can_make_a_payment_with_required_values(self):
        form = MakePaymentForm({
                    'credit_card_number': '4242424242424242', 
                    'cvv': "111",
                    'expiry_month': 1,
                    'expiry_year': 2020,
                    'stripe_id': 'l'
        })
        self.assertTrue(form.is_valid())
        
    
    def test_cannot_make_a_payment_without_required_values(self):
        form = MakePaymentForm({
                    'credit_card_number': '4242424242424242', 
                    'cvv': '', 
                    'expiry_month': 1,
                    'expiry_year': 2020,
        })
        self.assertFalse(form.is_valid())
        
class TestOrderForm(TestCase):
    
    def test_can_make_a_payment_with_required_values(self):
        form = OrderForm({
                    'full_name': "Test Testing", 
                    'email': 'test@test.com'
                    
        })
        self.assertTrue(form.is_valid())
        
        
    def test_cannot_make_a_payment_without_required_values(self):
        form = OrderForm({
                    'full_name': "Test Testing", 
                    'email': ''
                    
        })
        self.assertFalse(form.is_valid())