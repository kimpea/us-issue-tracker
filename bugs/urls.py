from django.conf.urls import url, include
from .views import bugs

urlpatterns = [
    url(r'^$', bugs, name="bugs")
]