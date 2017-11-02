from django.conf.urls import url

from . import views

# Url mappings - Routing

# Could use the following namespace
# app_name = "polls"  # to wire on urls like polls.detail ...

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),

    ## Generic way...
    # url(r'^$', views.index, name='index'),
    # # ex: /polls/1/
    # url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),

    # # ex: /polls/1/results/
    # url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),

    # # ex: /polls/1/vote/
    # url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]
