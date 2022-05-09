

from .views import *



from django.urls import path

urlpatterns = [
    path('signin/', signin),
    path('signup/',signup,name='signup')
  
]