from django.apps import apps
from django.test import TestCase, Client
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from features.models import Feature, FeatureComments
from django.utils import timezone

class TestFeatureViews(TestCase):
    
    def setUp(self):
        self.user = User.objects.create(username='Test',
                                        password='testing456')
        self.user.set_password('testing456')
        self.user.save()
        self.client = Client()
        self.client.login(username='Test',
                        password='testing456')
        self.feature = Feature.objects.create(name='Feature Name',
                                            description='Feature Description',
                                            user=self.user)
        self.feature.save()