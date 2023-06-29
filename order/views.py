from django.contrib.auth.models import User
from django.shortcuts import render
from product.models import Product
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Order, OrderItem
from .serializers import OrderItemSerializer, OrderSerializer


@api_view(['POST'])
def order_create(request):
	serializer = OrderSerializer(data=request.data)
	userId = request.data.get('userId')
	user = User.objects.get(id=userId)
	total_ammount = request.data.get('total_ammount')
	if serializer.is_valid():
		order = serializer.save(user=user, paid=True, total_ammount=total_ammount)

		cart_products = request.data.get('cartProducts', [])
		for cart_product in cart_products:
			productId = cart_product.get('id')
			quantity = cart_product.get('quantity')
			product = Product.objects.get(id=productId)

			OrderItem.objects.create(order=order, product=product, quantity=quantity)

		return Response(serializer.data, status=status.HTTP_201_CREATED)
	return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_orders(request, pk):
	try:
		user = User.objects.get(pk=pk)
		orders = Order.objects.filter(user=user)
		order_items = OrderItem.objects.filter(order__in=orders)
		total_spent = sum(order.total_ammount for order in orders)

		data = []
		for item in order_items:
			item_data = {
				'orderId':item.order.id,
				'productName': item.product.name,
				'productPrice': item.product.price,
				'productQuantity': item.quantity,
				'orderAddress': item.order.address,
				'orderTotal': item.order.total_ammount,
			}
			data.append(item_data)
		cards_data = {'totalSpent': total_spent,}

		return Response({'orders': data, 'cards_data': cards_data}, status=status.HTTP_200_OK)
	except User.DoesNotExist:
		return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
	except Exception as e:
		return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
def all_orders(request):
	order_items = OrderItem.objects.all()
	all_orders = Order.objects.all()
	total_profits = sum(order.total_ammount for order in all_orders)
	data = []
	for item in order_items:
		item_data = {
			'orderId':item.order.id,
			'productName': item.product.name,
			'productPrice': item.product.price,
			'productQuantity': item.quantity,
			'orderAddress': item.order.address,
			'orderTotal': item.order.total_ammount,
		}
		data.append(item_data)
	cards_data = {'totalProfits': total_profits,}
	
	return Response({'orders': data, 'cards_data': cards_data}, status=status.HTTP_200_OK)
