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
			'id',
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
	def to_representation(self, instance):
		many = isinstance(instance, list) # checking if instance is a single object or a list
		if self.context.get('request').method == 'POST': # remove id field from serialization if creating a new order
			self.fields.pop('id', None)
		return super().to_representation(instance)
