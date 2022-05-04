from nbformat import read
from rest_framework import serializers
from products.models import Product, ProductComment
from users.models import Supplier


class ProductSerializer(serializers.ModelSerializer):
    supplier = serializers.ReadOnlyField("supplier.name")
    productComment = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    category = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    
    class Meta:
        model = Product
        fields = '__all__'
        
        
class ProductCommentSerializer(serializers.ModelSerializer):
    product = serializers.ReadOnlyField('product.name')
    user = serializers.ReadOnlyField('user.username')
    
    class Meta:
        model = ProductComment
        fields = '__all__'