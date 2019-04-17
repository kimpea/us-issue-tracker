from django.conf.urls import url, include
from .views import features, feature_detail, request_feature, feature_comment

urlpatterns = [
    url(r'^$', features, name="features"),
    url(r'^feature_detail/(?P<id>\d+)/$', feature_detail, name="feature_detail"),
    url(r'^request_feature/$', request_feature, name='request_feature'),
    url(r'^feature_comment/(?P<id>\d+)/$', feature_comment, name='feature_comment'),
]