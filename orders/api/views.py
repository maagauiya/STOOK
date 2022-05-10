from orders.api.serializers import OrderSerializer
from orders.models import Order
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from cart.models import CartItem
from rest_framework import status


@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def create_orders(request):
    user = request.user
    data = request.data
    cart = CartItem.objects.filter(user=user)
    
    if cart.first() == None:
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
    