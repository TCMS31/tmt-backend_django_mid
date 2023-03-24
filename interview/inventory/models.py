from django.db import models

from interview.core.behaviors import IsActiveModel, NameModel, TimestampedModel, UniqueNameModel


class InventoryTag(UniqueNameModel, TimestampedModel, IsActiveModel, models.Model):
        
    def __str__(self) -> str:
        return self.name


class InventoryLanguage(UniqueNameModel, TimestampedModel, models.Model):

    class Meta:
        verbose_name_plural = 'Inventory Languages'
        
    def __str__(self) -> str:
        return self.name
    

class InventoryType(UniqueNameModel, TimestampedModel, models.Model):

    class Meta:
        verbose_name_plural = 'Inventory Types'
    
    def __str__(self) -> str:
        return self.name


class Inventory(NameModel, TimestampedModel, models.Model):
    type = models.ForeignKey(
        InventoryType,
        on_delete=models.CASCADE,
        related_name='inventories'
    )
    language = models.ForeignKey(
        InventoryLanguage,
        on_delete=models.CASCADE,
        related_name='inventories'
    )
    tags = models.ManyToManyField(InventoryTag, related_name='inventories')
    metadata = models.JSONField()
    
    class Meta:
        verbose_name_plural = 'Inventories'

    def __str__(self) -> str:
        return self.name
    
    @classmethod
    def get_by_type(cls, type_id: int):
        return cls.objects.filter(type_id=type_id)
    
    @classmethod
    def get_by_language(cls, language_id: int):
        return cls.objects.filter(language_id=language_id)