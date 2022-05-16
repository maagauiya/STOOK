from django.db import models
from django.contrib.auth.models import User
from products.models import Product

# Create your models here.
class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    total = models.FloatField(blank=True, null=True)
    name = models.CharField(max_length=50,blank=True, null=True)
    image_path = models.CharField(max_length=100,blank=True, null=True)
