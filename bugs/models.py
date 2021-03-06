from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Bug(models.Model):
    STATUS_CHOICES = (
        ('OPEN', 'OPEN'),
        ('IN PROGRESS', 'IN PROGRESS'),
        ('FIXED', 'FIXED')
    )
    name = models.CharField(max_length=254, default=None)
    description = models.TextField()
    user = models.ForeignKey(User, default=None)
    date_created = models.DateTimeField(auto_now_add=True)
    open_date = models.DateTimeField(blank=True, default=None, null=True)
    in_progress_date = models.DateTimeField(blank=True, default=None, null=True)
    fixed_date = models.DateTimeField(blank=True, default=None, null=True)
    upvotes = models.IntegerField(default=0)
    status = models.CharField(choices=STATUS_CHOICES, default='OPEN', max_length=20)

    def __str__(self):
        return self.name
        
class BugComments(models.Model):
    bug = models.ForeignKey(Bug, null=True)
    user = models.ForeignKey(User, null=None)
    comment = models.TextField(blank=False)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment