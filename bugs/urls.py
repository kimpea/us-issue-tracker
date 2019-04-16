from django.conf.urls import url, include
from .views import bugs, bug_detail, report_bug, upvote_bug, bug_comment

urlpatterns = [
    url(r'^$', bugs, name="bugs"),
    url(r'^bug_detail/(?P<id>\d+)/$', bug_detail, name="bug_detail"),
    url(r'^(?P<id>\d+)/upvote_bug/$', upvote_bug, name='upvote_bug'),
    url(r'^report_bug/$', report_bug, name='report_bug'),
    url(r'^bug_comment/(?P<id>\d+)/$', bug_comment, name='bug_comment'),
]