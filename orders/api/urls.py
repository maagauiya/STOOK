from django.urls import path
from . import views

urlpatterns = [
    path('create-orders/', views.create_orders, name='create_orders'),
    
]
