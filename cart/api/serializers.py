from rest_framework import serializers
from rest_framework.decorators import api_view
from cart.models import CartItem


class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = '__all__'