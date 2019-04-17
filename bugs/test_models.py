from django.test import TestCase
from .models import Bug
from django.contrib.auth.models import User

# Create your tests here.
class TestBug(TestCase):
    def test_str(self):
        test_name = Bug(name='A bug')
        self.assertEqual(str(test_name), 'A bug')
        
    def test_report_bug(self):
            user = User()
            user.save()
            bug = Bug(name="Bug", description="Bug Description", user=user)
            bug.save()
            self.assertEqual(bug.name, "Bug")
            self.assertEqual(bug.description, "Bug Description")
            self.assertEqual(bug.user, user)
            self.assertEqual(bug.status, "OPEN")
            self.assertEqual(bug.upvotes, 0)