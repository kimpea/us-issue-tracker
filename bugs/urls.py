from django.conf.urls import url, include
from .views import bugs, bug_detail, report_bug

urlpatterns = [
    url(r'^$', bugs, name="bugs"),
    url(r'^bug_detail/(?P<id>\d+)/$', bug_detail, name="bug_detail"),
    url(r'^report_bug/$', report_bug, name='report_bug'),
]