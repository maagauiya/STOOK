from django.urls import path, include
from . import views

urlpatterns = [
    path('add/', views.add_in_cart, name='add_in_cart'),
    path('user-cart/', views.get_user_cart, name='get_user_cart'),
    path('edit-cart-item/<int:pk>', views.edit_cart_item, name='edit_cart_item'),
    path('delete-cart-item/<int:pk>', views.delete_cart_item, name='delete_cart_item'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
