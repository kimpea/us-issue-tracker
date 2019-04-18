from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Question(models.Model):
    question = models.CharField(max_length=254, default='')
    description = models.TextField(blank=True)
    user = models.ForeignKey(User, default=None)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question