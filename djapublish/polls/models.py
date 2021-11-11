
import datetime
import os,sys
from django.db import models
from django.utils import timezone

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def pub_timeago(self):
        return timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


# Need to set env vars to make this work

def __main__(self):

    q = Question.objects.get(pk=1)

    q.choice_set.all()
    q.choice_set.create(choice_text='Not much', votes=0)
    q.choice_set.create(choice_text='The sky', votes=0)

    c = q.choice_set.create(choice_text='Just writing code', votes=0)

    # Choice objects have API access to their related Question objects.
    c.question

    # And vice versa: Question objects get access to Choice objects.
    q.choice_set.all()
    q.choice_set.count()
    # equals the SELECT command
    Choice.objects.filter(question__pub_date__year=current_year)
