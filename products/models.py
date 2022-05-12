from django.db import models
from users.models import UserProfile
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(primary_key=True, max_length=150, null=False, blank=False)
    
    def __str__(self):
        return self.name

class Product(models.Model):
   # supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, blank=True, null=True, related_name='categories', on_delete=models.SET_NULL)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50, blank=True, null=True)
    image = models.ImageField(blank=True, null=True)
    price = models.FloatField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name

    def __str__(self):
        return self.name

class ProductComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    body = models.CharField(max_length=150)
    created = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField()
    
    def __str__(self):
        return str(self.user.username)

    

