from products.models import Product, ProductComment
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import generics
from products.models import Product
from users.models import Supplier
from .serializers import ProductSerializer
from rest_framework.decorators import api_view


    