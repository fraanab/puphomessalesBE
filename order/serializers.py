from django.contrib.auth.models import User
from product.models import Product
from rest_framework import serializers

from .models import Order, OrderItem


class OrderItemSerializer(serializers.ModelSerializer):
	class Meta:
		model = OrderItem
		fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
	# order_items = OrderItemSerializer(many=True, read_only=True)
	class Meta:
		model = Order
		fields = [
			'ID',
			'total_ammount', 
			'first_name', 
			'last_name', 
			'address',
			'company',
			'building',
			'city',
			'phone',
			'email',
			'username',
		]
		# fields = '__all__'
