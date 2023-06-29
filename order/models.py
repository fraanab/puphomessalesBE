import uuid

from django.contrib.auth.models import User
from django.db import models
from product.models import Product


class Order(models.Model):
    orderid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    total_ammount = models.IntegerField(default=0)                          # set this to the total amount
    paid = models.BooleanField(default=False)                               # set this to true if paid

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.CharField(max_length=250)
    company = models.CharField(max_length=100, null=True, blank=True)
    building = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100)
    phone = models.CharField(max_length=100, null=True, blank=True)

    email = models.EmailField()
    username = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='orders')  # set this to the user using it's requested id

    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Order by {self.username} | Date {self.created} | Paid ${self.total_ammount} : {self.paid} | {self.orderid}'

class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True, blank=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)

    def __str__(self):
        return self.id
