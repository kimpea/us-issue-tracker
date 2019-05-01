from django.db import models
from features.models import Feature

# Create your models here.

class Order(models.Model):
    full_name = models.CharField(max_length=50, blank=False)
    email = models.EmailField(max_length=100, blank=False, default='example@example.com')
    
    def __str__(self):
        return "{0}-{1}-{2}".format(self.id, self.full_name, self.email)
        
        
class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, null=False)
    feature = models.ForeignKey(Feature, null=False, default="Feature")
    quantity = models.IntegerField(blank=False)
    
    def __str__(self):
        return "{0} {1} @ {2}".format(self.quantity, self.feature.name, self.feature.price)