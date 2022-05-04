from django.db import models
from users.models import Supplier, UserProfile

# Create your models here.
class Category(models.Model):
    name = models.CharField(primary_key=True, max_length=150, null=False, blank=False)
    
    def __str__(self):
        return self.name

class Product(models.Model):
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category, blank=True, related_name='categories')
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50, blank=True, null=True)
    image = models.ImageField()
    price = models.FloatField()

class ProductComment(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    body = models.CharField(max_length=150)
    rating = models.IntegerField()

