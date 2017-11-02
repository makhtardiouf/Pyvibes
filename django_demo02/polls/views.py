from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Question, Choice

# Using Django's generic views here. Role of Controllers


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'qlist'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-publi_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    ... # same as above, no changes needed.
