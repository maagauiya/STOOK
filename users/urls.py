

from unicodedata import name
from .views import *
from django.contrib.auth import views as auth_views

from django.urls import path, include

from django.urls import path

urlpatterns = [
    path('', signin,name='signin'),
    path('signup/',signup,name='signup'),
    path('account/',account_page,name='profile'),
    path('reset_password/',
     auth_views.PasswordResetView.as_view(template_name="users/reset_pass.html"),
     name="reset_password"),

    path('reset_password_sent/', 
        auth_views.PasswordResetDoneView.as_view(template_name="users/email_sent.html"), 
        name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
     auth_views.PasswordResetConfirmView.as_view(template_name="users/email_reset_form.html"), 
     name="password_reset_confirm"),

    path('reset_password_complete/', 
        auth_views.PasswordResetCompleteView.as_view(template_name="users/email_done.html"), 
        name="password_reset_complete"),
    path('account-info/',account_info, name='account_info'),
    path('account-address/',account_address, name='account_address'),
    path('account_new_address/',account_new,name='account_new'),
    path('account_orders/',account_orders,name='account_orders'),
    path('account_news/',account_news,name='account_news'),
    path('account_wishlist/',account_wishlist,name='account_wishlsit'),
    path('index/',index, name='index'),
    path('product/<int:number>',product_page,name='product_page'),
    path('order/<int:pk>', order, name="order"),
    path('remove/<int:pk>', remove_from_cart, name="remove" ),
    path('payment/<int:pk>',payment, name='payment'),


]