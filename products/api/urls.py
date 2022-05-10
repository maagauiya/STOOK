from django.urls import path, include
from . import views

urlpatterns = [
    path('<int:pk>/', views.get_product, name='product_detail'),
    path('', views.get_products, name='product_list'),
    path('create/', views.create_product, name='create_product'),
    path('edit/<int:pk>/', views.edit_product, name='edit_product'),
    path('delete/<int:pk>/', views.delete_product, name='delete_product'),
    path('create-comment/<int:pk>', views.create_comment, name='create_comment'),
    path('get-comments/<int:pk>', views.get_comments, name='get_comments'),
    path('delete-comment/<int:pk>', views.delete_comment, name='delete_comment'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
