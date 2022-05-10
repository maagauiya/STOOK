

from unicodedata import name
from .views import *
from django.contrib.auth import views as auth_views

from django.urls import path, include

from django.urls import path

urlpatterns = [
    path('signin/', signin,name='signin'),
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
]