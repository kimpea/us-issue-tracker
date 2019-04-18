from django.test import TestCase
from .models import Order
from datetime import datetime

class TestOrderModel(TestCase):
    def test_create_order_with_details(self):
        order = Order(full_name="Test Testing", email='test@test.com')
        order.save()
        self.assertEquals(order.full_name, "Test Testing")
        self.assertEquals(order.email, "test@test.com")