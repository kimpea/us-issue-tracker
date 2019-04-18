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
        
        
    def test_get_all_features(self):
        """
        Testing features view which displays all features 
        """
        page=self.client.get("/features/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "features.html")
        
    
    def test_get_feature_detail_page(self):
        """
        Testing single feature detail view 
        """
        user = User.objects.create_user(username='USER1', password='testing123')
        user.save()
        feature = Feature(name='Feature', description='Testing', user=user, price=20, upvotes=0, status='INCOMPLETE')
        feature.save()
        page = self.client.get('/features/feature_detail/1', follow=True)
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "feature_detail.html")