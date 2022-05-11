from django.urls import path
from . import views

urlpatterns = [
    path('create-orders/', views.create_orders, name='create_orders'),
    path('edit-order/<int:pk>', views.edit_order, name='edit_order')
]
