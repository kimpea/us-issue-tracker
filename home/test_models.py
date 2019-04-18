from django.test import TestCase
from .models import Question
from django.contrib.auth.models import User

# Create your tests here.
class TestQuestion(TestCase):
    """
    Here we'll define the tests that we'll run against our
    Feature model
    """

    def test_str(self):
        test_name = Question(question='A question')
        self.assertEqual(str(test_name), 'A question')
        
    def test_ask_question(self):
        user = User()
        user.save()
        question = Question(question="Question", description="Question Description", user=user)
        question.save()
        self.assertEqual(question.question, "Question")
        self.assertEqual(question.description, "Question Description")