from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Feature(models.Model):
    STATUS_CHOICES = (
        ('INCOMPLETE', 'INCOMPLETE'),
        ('IN PROGRESS', 'IN PROGRESS'),
        ('COMPLETE', 'COMPLETE')
    )
    name = models.CharField(max_length=254, default=None)
    description = models.TextField(blank=False)
    user = models.ForeignKey(User, default=None)
    date_created = models.DateTimeField(auto_now_add=True)
    incomplete_date = models.DateTimeField(blank=True, default=None, null=True)
    in_progress_date = models.DateTimeField(
        blank=True, default=None, null=True)
    completed_date = models.DateTimeField(blank=True, default=None, null=True)
    upvotes = models.IntegerField(default=0)
    status = models.CharField(choices=STATUS_CHOICES, default='INCOMPLETE', max_length=20)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=20)

    def __str__(self):
        return self.name


class FeatureComments(models.Model):
    feature = models.ForeignKey(Feature, null=True)
    user = models.ForeignKey(User, null=None)
    comment = models.TextField(blank=False)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment