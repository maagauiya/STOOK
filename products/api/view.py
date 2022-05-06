from products.models import Product, ProductComment
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import generics, permissions
from products.models import Product
from .serializers import ProductSerializer
from rest_framework.decorators import api_view
from django.db.models import Q
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated


# @api_view(['GET'])
# def get_products(request):
#     query = request.query_params.get('q')
#     if query == None:
#         query = ''
        
#     products = Product.objects.filter()



# class ProductList(generics.ListCreateAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     #permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    
# class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#   #  №permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    
@api_view(['GET'])
def get_product(request, pk):
    try:
        product = Product.objects.get(id=pk)
        serializer = ProductSerializer(product, many=False)
        return Response(serializer.data)
    except Exception as e:
        return Response({'details': f"{e}"},status=status.HTTP_204_NO_CONTENT)
    
@api_view(['GET'])
def get_products(request):
    query= request.query_params.get('q')
    if query == None:
        query = ''
    products = Product.objects.filter(Q(name__icontains=query))
    paginator = PageNumberPagination()
    paginator.page_size = 10
    result_page = paginator.paginate_queryset(products, request)
    serializer = ProductSerializer(result_page, many=True)
    return paginator.get_paginated_response(serializer.data)


@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def create_product(request):
    user = request.user
    data = request.data
    
    category = data.get('category')
    name = data.get('name')
    description = data.get('description')
    image = data.get('image')
    price = data.get('price')
    
    product = Product.objects.create(
        user = user,
        category = category,
        name = name,
        description = description,
        image = image,
        price = price,
    )
    
    product.save()
    serializer = ProductSerializer(product, many=False)
    return Response(serializer.data)