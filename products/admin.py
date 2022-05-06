from django.contrib import admin
from .models import Product, ProductComment, Category

# Register your models here.

admin.site.register(Product)
admin.site.register(ProductComment)
admin.site.register(Category)