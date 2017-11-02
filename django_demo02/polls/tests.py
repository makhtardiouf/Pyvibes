# Create your tests here.
import datetime

from django.utils import timezone
from django.test import TestCase
from .models import Question

class QuestionModelTests(TestCase):

    def test_was_published_recently(self):
        """
        was_published_recently() returns False for questions whose publi_date
        is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        q = Question(publi_date=time)
        self.assertIs(q.is_recent(), False)
 