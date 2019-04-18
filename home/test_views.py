from django.apps import apps
from django.test import TestCase, Client
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from home.models import Question
from django.utils import timezone

class TestHomeViews(TestCase):
    
    def test_get_index_page(self):
        """
        Testing index view which is the first page user sees
        """
        page=self.client.get("/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "index.html")
        
        
    def test_get_about_page(self):
        """
        Testing about view
        """
        page=self.client.get("/about/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "about.html")