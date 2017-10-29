from django.conf.urls import url

from . import views

# Url mappings 

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
