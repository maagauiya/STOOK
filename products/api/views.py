from email.quoprimime import body_check
from django.shortcuts import get_object_or_404
from products.models import Category, Product, ProductComment
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import generics, permissions
from products.models import Product
from .serializers import ProductCommentSerializer, ProductSerializer
from rest_framework.decorators import api_view
from django.db.models import Q
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated

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
        name = name,
        description = description,
        image = image,
        price = price,
    )
    if category != None:
        category = find_or_create_category(category)
    product.category = category
    product.save()
    serializer = ProductSerializer(product, many=False)
    return Response(serializer.data)


def find_or_create_category(category):
    try:
        _category = Category.objects.get(name=category)
    except Exception as e:
        _category = Category.objects.create(name=category)
        _category.save()
    return _category
    

@api_view(['DELETE'])
@permission_classes((IsAuthenticated,))
def delete_product(request, pk):
    try:
        product = Product.objects.get(id=pk)
        if product.user == request.user:
            product.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
    except Exception as e:
        return Response({'details':f"{e}"}, status=status.HTTP_204_NO_CONTENT)
    
@api_view(['PUT'])
@permission_classes((IsAuthenticated,))
def edit_product(request, pk):
    try:
        product = Product.objects.get(id=pk)
        if product.user == request.user:
            data = request.data
            product.name = data.get('name')
            product.description = data.get('description')
            product.image = data.get('image')
            product.price = data.get('price')
            product.category = find_or_create_category(data.get('category'))
            product.save()
            serializer = ProductSerializer(product, many=False)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
    except Exception as e:
        return Response({'details': f"{e}"},status=status.HTTP_204_NO_CONTENT)



@api_view(['GET'])
def get_comments(request, pk):
    comments = ProductComment.objects.filter(product=pk)
    serializer = ProductCommentSerializer(comments, many=True)
    return Response(serializer.data)
    

@api_view(['DELETE'])
@permission_classes((IsAuthenticated,))
def delete_comment(request, pk):
    comment = get_object_or_404(ProductComment, id=pk)
    if comment.user == request.user:
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        return Response(status=status.HTTP_401_UNAUTHORIZED)


@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def create_comment(request, pk):
    user = request.user
    data = request.data
    
    product = get_object_or_404(Product, id=pk)
    body = data.get('body')
    rating = data.get('rating')
    
    comment = ProductComment.objects.create(
        user = user,
        product = product,
        body = body,
        rating = rating
    )
    comment.save()
    serializer = ProductCommentSerializer(product, many=False)
    return Response(serializer.data)