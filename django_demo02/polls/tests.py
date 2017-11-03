# Create your tests here.
import datetime

from django.utils import timezone
from django.test import TestCase
from .models import Question

class QuestionModelTests(TestCase):

    def test_publication_is_recent(self):
        """
        is_recent() returns False for questions whose publi_date
        is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        q = Question(publi_date=time)
        self.assertIs(q.is_recent(), False)
 

    def test_is_recent_with_old_question(self):
        """
        is_recent() returns False for questions whose publi_date
        is older than 1 day.
        """
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_question = Question(publi_date=time)
        self.assertIs(old_question.is_recent(), False)


    def test_is_recent_with_recent_question(self):
        """
        is_recent() returns True for questions whose publi_date
        is within the last day.
        """
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_question = Question(publi_date=time)
        self.assertIs(recent_question.is_recent(), True)
