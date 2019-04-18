from django.test import TestCase
from django.contrib.auth.models import User
from .views import index, login, logout, register
from django.test.client import Client
from django.core.urlresolvers import reverse