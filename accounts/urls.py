from django.conf.urls import url, include
from accounts.views import index, logout, login, register, user_profile

urlpatterns = [
    url(r'^logout/$', logout, name="logout"),
    url(r'^login/$', login, name="login"),
    url(r'^register/$', register, name="register"),
    url(r'^profile/$', user_profile, name="profile"),
]