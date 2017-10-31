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

    template = loader.get_template('polls/index.html')
    context = {'qlist' : qlist, }
    return HttpResponse(template.render(context, request))
    #return HttpResponse("Welcome to Makhtar's demo Polling app. Here are the latest questions:<br>" + resp)

def detail(request, question_id):
    logging.info("This a log test")

    question = Question.objects.get(pk=question_id)
    context = {'question': question}
    return render(request, 'polls/detail.html', context)
    #return HttpResponse(str(datetime.now()) + ": You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
