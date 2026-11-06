from rest_framework import serializers
from .models import Category, Service, Order

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description']

class ServiceSerializer(serializers.ModelSerializer):
    owner_username = serializers.ReadOnlyField(source='owner.username')
    category_name = serializers.ReadOnlyField(source='category.name')

    class Meta:
        model = Service
        fields = [
            'id', 'title', 'description', 'price',
            'category', 'category_name', 'owner', 'owner_username', 'created_at'
        ]
        read_only_fields = ['owner', 'created_at']

class OrderSerializer(serializers.ModelSerializer):
    service_title = serializers.ReadOnlyField(source='service.title')
    customer_username = serializers.ReadOnlyField(source='customer.username')

    class Meta:
        model = Order
        fields = [
            'id', 'service', 'service_title', 'customer', 'customer_username',
            'status', 'created_at', 'updated_at'
        ]
        read_only_fields = ['customer', 'created_at', 'updated_at']