from django.urls import path

from . import views

urlpatterns = [
	path('make-order/', views.order_create, name="make-order"),
	path('get-orders/<int:pk>/', views.get_orders, name="get-orders"),			# using the User id, not the Order id
	path('get-all-orders/', views.all_orders, name="get-all-orders"),
]
