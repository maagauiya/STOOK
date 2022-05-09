from rest_framework import serializers
from products.models import Product, ProductComment, Category
from users.api.serializers import UserProfileSerializer


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
   # productComment = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
   # category = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    user = serializers.SerializerMethodField(read_only=True)
    category = CategorySerializer(many=False)
    
    class Meta:
        model = Product
        fields = '__all__'
        
    def get_user(self, obj):
        user = obj.user.userprofile
        serializer = UserProfileSerializer(user, many=False)
        return serializer.data['username']
        
        
class ProductCommentSerializer(serializers.ModelSerializer):
   # product = serializers.ReadOnlyField('product.name')
   # user = serializers.ReadOnlyField('user.username')
    user = serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        model = ProductComment
        fields = '__all__'
        
    def get_user(self, obj):
        user = obj.user.userprofile
        serializer = UserProfileSerializer(user, many=True)
        return serializer.data
        
        
