from django.test import TestCase
from .models import Feature, FeatureComments
from django.contrib.auth.models import User

# Create your tests here.
class TestFeature(TestCase):
    """
    Here we'll define the tests that we'll run against our
    Feature model
    """

    def test_str(self):
        test_name = Feature(name='A feature')
        self.assertEqual(str(test_name), 'A feature')
        
    def test_request_feature(self):
        user = User()
        user.save()
        feature = Feature(name="Feature", description="Feature Description", user=user)
        feature.save()
        self.assertEqual(feature.name, "Feature")
        self.assertEqual(feature.description, "Feature Description")
        self.assertEqual(feature.user, user)
        self.assertEqual(feature.price, 20)
        self.assertEqual(feature.status, "INCOMPLETE")
        self.assertEqual(feature.upvotes, 0)
        
    def test_add_comment(self):
        user = User()
        user.save()
        feature = Feature(name="Feature", description="Feature Description", user=user, price=20)
        feature.save()
        comment = FeatureComments(comment="Feature Comment", user=user, feature=feature)
        comment.save()
        self.assertEqual(comment.comment, "Feature Comment")
        self.assertEqual(comment.user, user)
        self.assertEqual(comment.feature, feature)