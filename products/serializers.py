from dataclasses import field
from socket import CAN_RAW
from rest_framework import  serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'description', 'price', 'inventory_quantity']