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