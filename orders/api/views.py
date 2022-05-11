from orders.api.serializers import OrderSerializer
from orders.models import Order
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from cart.models import CartItem
from rest_framework import status
from django.shortcuts import get_object_or_404
from products.models import Product


@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def create_orders(request):
    user = request.user
    data = request.data
    
    cart = CartItem.objects.filter(user=user)
    if cart.first() == None:
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    country = data.get('country')
    region = data.get('region')
    city = data.get('city')
    address = data.get('address')
    post_number = data.get('post_number')
    _status = 'Ordered, waiting supplier confirmation'
    
    orders = []
    
    for i in cart:
        product = get_object_or_404(Product, id=i.product.id)
        supplier = product.user
        quantity = i.quantity
        
        order = Order.objects.create(
            client = user,
            supplier = supplier,
            product = product,
            quantity = quantity,
            country = country,
            region = region,
            city = city,
            address = address,
            post_number = post_number,
            status = _status
        )
        order.save()
        i.delete()
        orders.append(order)
        
    _orders = Order.objects.filter(id__in=[i.id for i in orders])
    serializer = OrderSerializer(_orders, many=True)
    return Response(serializer.data)
        

@api_view(['PUT'])
@permission_classes((IsAuthenticated,))
def edit_order(request, pk):
    data = request.data
    order = get_object_or_404(Order, id=pk)
    if order.supplier == request.user:
        if data.get('status'):
            order.status = data.get('status')
        
        if data.get('track_number'):
            order.track_number = data.get('track_number')
            
        if data.get('shipping_date'):
            order.shipping_date = data.get('shipping_date')    
        
        order.save()
        serializer = OrderSerializer(order, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_401_UNAUTHORIZED)

        

    
    
    
    