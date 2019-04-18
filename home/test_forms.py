from django.test import TestCase
from .forms import FAQForm


class TestQuestionForm(TestCase):

    def test_question_has_name_and_description(self):
        form = FAQForm(
            {'question': 'Question',
            'description': 'Description'})
        self.assertTrue(form.is_valid())