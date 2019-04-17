from django.apps import apps
from django.test import TestCase, Client
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from bugs.models import Bug, BugComments
from django.utils import timezone

class TestBugViews(TestCase):
    
    def setUp(self):
        self.user = User.objects.create(username='Test',
                                        password='testing456')
        self.user.set_password('testing456')
        self.user.save()
        self.client = Client()
        self.client.login(username='Test',
                        password='testing456')
        self.bug = Bug.objects.create(name='Bug Name',
                                            description='Bug Description',
                                            user=self.user)
        self.bug.save()
       
        
    def test_get_all_bugs(self):
        """
        Testing bugs view which displays all bugs 
        """
        page=self.client.get("/bugs/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "bugs.html")
        
        
    def test_get_bug_detail_page(self):
        """
        Testing single bug detail view 
        """
        user = User.objects.create_user(username='USER1', password='testing123')
        user.save()
        bug = Bug(name='Bug', description='Testing', user=user, upvotes=0, status='INCOMPLETE')
        bug.save()
        page = self.client.get('/bugs/bug_detail/1', follow=True)
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "bug_detail.html") 