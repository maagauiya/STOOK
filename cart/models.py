from django.db import models
from django.contrib.auth.models import User
from products.models import Product

# Create your models here.
class CartItem(models.Model):
    client_id = models.ForeignKey(User, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
