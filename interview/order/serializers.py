from rest_framework import serializers
from interview.inventory.serializers import InventorySerializer

from interview.order.models import Order, OrderTag


class OrderTagSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = OrderTag
        fields = ['id', 'name', 'is_active']


class OrderSerializer(serializers.ModelSerializer):
    inventory = InventorySerializer()
    tags = OrderTagSerializer(many=True)
    
    class Meta:
        model = Order
        fields = ['id', 'inventory', 'start_date', 'embargo_date', 'tags', 'is_active']