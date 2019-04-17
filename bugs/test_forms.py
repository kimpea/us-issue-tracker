from django.test import TestCase
from .forms import ReportBugForm, BugCommentForm

class TestReportBugForm(TestCase):

    def test_bug_has_name_and_description(self):
        form = ReportBugForm(
            {'name': 'Bug Name',
            'description': 'Bug Description'})
        self.assertTrue(form.is_valid())
        
    def test_bug_without_name_or_description(self):
        form = ReportBugForm({
            'name': 'Bug Name',
            'description': ''
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['description'], ['This field is required.'])
        
class TestBugCommentForm(TestCase):
    
    def test_bug_comment_form(self):
        form = BugCommentForm({'comment': 'This is a comment'})
        self.assertTrue(form.is_valid())