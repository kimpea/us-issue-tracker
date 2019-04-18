from django.test import TestCase
from django.contrib.auth.models import User
from .views import index, login, logout, register
from django.test.client import Client
from django.core.urlresolvers import reverse

class TestViews(TestCase):
    
    # Home Page
    def test_get_home_page(self):
        page = self.client.get("/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "index.html")