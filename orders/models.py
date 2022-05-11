from ctypes import addressof
from django.db import models
from products.models import Product
from django.contrib.auth.models import User

# Create your models here.

class Order(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE, related_name='clients')
    supplier = models.ForeignKey(User, on_delete=models.CASCADE, related_name='suppliers')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    country = models.CharField(max_length=50)
    region = models.CharField(max_length=50)
    city = models.CharField(max_length=50, default='')
    address = models.CharField(max_length=200)
    post_number = models.CharField(max_length=50)
    price = models.FloatField(blank=True, null=True)
    track_number = models.IntegerField(blank=True, null=True)
    order_date = models.DateTimeField(auto_now_add=True)
    shipping_date = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=50)