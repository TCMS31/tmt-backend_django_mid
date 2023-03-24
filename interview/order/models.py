from django.db import models

from interview.core.behaviors import IsActiveModel, TimestampedModel, UniqueNameModel
from interview.inventory.models import Inventory


class OrderTag(UniqueNameModel, TimestampedModel, IsActiveModel, models.Model):
        
    def __str__(self) -> str:
        return self.name
    

class Order(TimestampedModel, IsActiveModel, models.Model):
    inventory = models.ForeignKey(
        Inventory,
        on_delete=models.CASCADE,
        related_name='orders'
    )
    start_date = models.DateField()
    embargo_date = models.DateField()
    tags = models.ManyToManyField(OrderTag, related_name='orders')
    
    def __str__(self) -> str:
        return f'{self.inventory.name} - {self.start_date}'