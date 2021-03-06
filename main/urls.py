from django.conf.urls import url

from . import views as main_views

urlpatterns = [
    # ex: /polls/
    url(r'^$', main_views.index, name='index'),
    # ex: /polls/5/
    url(r'^(?P<question_id>[0-9]+)/$', main_views.detail, name='detail'),
    # ex: /polls/5/results/
    url(r'^(?P<question_id>[0-9]+)/results/$', main_views.results, name='results'),
    # ex: /polls/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', main_views.vote, name='vote'),
]