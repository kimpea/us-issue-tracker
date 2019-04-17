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
        
    
    def test_get_report_bug_page(self):
        """
        Testing report_bug view
        """
        user = User.objects.create_user('TestingUser', 'testing@test.com', 'testing123')
        self.client.login(username='TestingUser', password='testing123')
        page = self.client.get("/bugs/report_bug/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'report_bug.html')
        
        
    def test_adding_a_new_bug_to_database(self):
        """
        Testing if bug is being added to database successfully
        """
        user = User.objects.create_user('TestingUser', 'testing@test.com', 'testing123')
        self.client.login(username='TestingUser', password='testing123')
        page = self.client.post('/bugs/report_bug/',
                                    {'name': 'new bug title',
                                     'description': 'this is a new description',
                                     'user': self.user,
                                     'date_created': timezone.now,
                                     'upvotes': 0,
                                     'status': 'INCOMPLETE',
                                     'price': 20,
                                    })
        bug = get_object_or_404(Bug, pk=2)
        self.assertEqual(bug.name, 'new bug title')
        self.assertEqual(bug.description, 'this is a new description')
        self.assertEqual(str(bug.user), 'TestingUser')
        self.assertEqual(bug.upvotes, 0)
        self.assertEqual(bug.status, 'OPEN')
        self.assertEqual(page.status_code, 302)
        
    
    def test_create_a_new_bug_comment(self):
        """
        Testing if user can successfully submit a bug comment 
        """
        user = User.objects.create_user('TestingUser', 'testing@test.com', 'testing123')
        self.client.login(username='TestingUser', password='testing123')
        page = self.client.post('/bugs/bug_comment/{0}/'.format(self.bug.id),
                                    {'bug': self.bug,
                                     'user': self.user,
                                     'date_created': timezone.now,
                                     'comment': "This is a bug comment"})

        comment = get_object_or_404(BugComments, pk=1)

        self.assertEqual(str(comment.bug), "Bug Name")
        self.assertEqual(str(comment.user), "TestingUser")
        self.assertEqual(comment.comment, "This is a bug comment")
        self.assertEqual(page.status_code, 302)