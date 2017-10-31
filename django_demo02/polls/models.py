import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class Question(models.Model):
    content = models.CharField(max_length=200)
    publi_date = models.DateTimeField('date published')

    def __str__(self):
        return self.content

    def is_recent(self):
        return self.publi_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice = models.TextField(max_length=200)
    votes = models.IntegerField(default=1)

    def __str__(self):
        return self.choice + ": " + str(self.votes)



# Need to set env vars to make this work

def __main__(self):

    q = Question.objects.get(pk=1)

    q.choice_set.all()
    q.choice_set.create(choice='Not much', votes=3)
    q.choice_set.create(choice='The sky', votes=2)

    c = q.choice_set.create(choice='Just code it', votes=15)

    # Choice objects have API access to their related Question objects.
    c.question

    # And vice versa: Question objects get access to Choice objects.
    q.choice_set.all()
    q.choice_set.count()
    # equals the SELECT command
    Choice.objects.filter(question__publi_date__year=current_year)

