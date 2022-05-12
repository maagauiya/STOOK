from .serializers import CartItemSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import generics, permissions
from rest_framework.decorators import api_view
from django.db.models import Q
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from cart.models import CartItem
from products.models import Product


@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def add_in_cart(request):
    user = request.user
    data = request.data
    
    product_id = data.get('product')
    quantity = data.get('quantity')
    
    product = get_object_or_404(Product, id=product_id)
    
    find_dup = CartItem.objects.filter(product=product).first()
    if find_dup != None:
        return Response(status=status.HTTP_451_UNAVAILABLE_FOR_LEGAL_REASONS)
    cart_item = CartItem.objects.create(
        user = user,
        product = product,
        quantity = quantity,
    )
    serializer = CartItemSerializer(cart_item, many=False)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def get_user_cart(request):
    user = request.user
    cart = CartItem.objects.filter(user=user)
    serializer = CartItemSerializer(cart, many=True)
    return Response(serializer.data)


@api_view(['PUT'])
@permission_classes((IsAuthenticated,))
def edit_cart_item(request, pk):
    cart_item = get_object_or_404(CartItem, id=pk)
    if cart_item.user == request.user:
        data = request.data
        cart_item.quantity = int(data.get('quantity'))
        cart_item.save()
        serializer = CartItemSerializer(cart_item, many=False)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_401_UNAUTHORIZED)
    

@api_view(['DELETE'])
@permission_classes((IsAuthenticated,))
def delete_cart_item(request, pk):
    cart_item = get_object_or_404(CartItem, id=pk)
    if cart_item.user == request.user:
        cart_item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        return Response(status=status.HTTP_401_UNAUTHORIZED)
    
    
    

    
    
