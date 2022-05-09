from django.urls import path, include
from . import view

urlpatterns = [
    path('<int:pk>/', view.get_product, name='product_detail'),
    path('', view.get_products, name='product_list'),
    path('create/', view.create_product, name='create_product'),
    path('edit/<int:pk>/', view.edit_product, name='edit_product'),
    path('delete/<int:pk>/', view.delete_product, name='delete_product'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
