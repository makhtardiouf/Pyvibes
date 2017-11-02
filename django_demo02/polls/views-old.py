from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

from datetime import datetime
from .models import Question, Choice

import logging

# Create your views here. Role of Controllers

def index(request):
    logging.info("This a log test")
    # Retrieve last 5 questions
    qlist = Question.objects.order_by('-publi_date')[:5]
    #resp = '<br>'.join([q.content for q in qlist])
    return render(request, 'polls/index.html', {'qlist' : qlist})
    

def detail(request, question_id):
    logging.info("Accessing question detail page")
    try:
        question = Question.objects.get(pk=question_id)    
    except Question.DoesNotExist:
        raise Http404("Question does not exist")

    return render(request, 'polls/detail.html', {'question': question})
   

def results(request, question_id):
    q = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': q})


def vote(request, question_id):
    #return HttpResponse("You're voting on question %s." % question_id)
    q = get_object_or_404(Question, pk=question_id)

    try:
        choice = q.choice_set.get(pk=request.POST['choice'])

    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': q,
            'error_msg': "You didn't select a choice.",
        })
    else:
        choice.votes += 1
        choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('results', args=(q.id,)))
