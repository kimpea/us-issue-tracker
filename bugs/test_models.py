from django.test import TestCase
from .models import Bug, BugComments
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
            
    def test_add_comment(self):
        user = User()
        user.save()
        bug = Bug(name="Bug", description="Bug Description", user=user)
        bug.save()
        comment = BugComments(comment="Bug Comment", user=user, bug=bug)
        comment.save()
        self.assertEqual(comment.comment, "Bug Comment")
        self.assertEqual(comment.user, user)
        self.assertEqual(comment.bug, bug)