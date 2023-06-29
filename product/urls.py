from django.urls import path

from . import views

urlpatterns = [
	path('get-products/', views.getProducts, name="get-products"),
	path('new-product/', views.newProduct, name="new-product"),
	path('delete-product/<str:id>/', views.deleteProduct, name="delete-product"),
]
