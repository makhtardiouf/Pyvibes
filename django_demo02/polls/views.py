from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from datetime import datetime
from .models import Question, Choice

import logging

# Create your views here. Role of Controllers

def index(request):
    logging.info("This a log test")
    # Retrieve last 5 questions
    qlist = Question.objects.order_by('-publi_date')[:5]
    #resp = '<br>'.join([q.content for q in qlist])

    # When not using the 'render' function
    template = loader.get_template('polls/index.html')
    context = {'qlist' : qlist, }
    return HttpResponse(template.render(context, request))
    #return HttpResponse(" Here are the latest questions:<br>" + resp)

def detail(request, question_id):
    logging.info("Accessing question detail page")
    try:
        question = Question.objects.get(pk=question_id)    
    except Question.DoesNotExist:
        raise Http404("Question does not exist")

    return render(request, 'polls/detail.html', {'question': question})
   
def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
