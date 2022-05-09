
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def signin(request):

    return render(request,'users/signin.html')