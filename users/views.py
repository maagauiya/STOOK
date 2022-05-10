
import time
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login ,logout
# Create your views here.
from django.contrib.auth.models import User
from .models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
def signin(request):
    

    if request.POST.get('login'):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/account/')
        else:
            messages.error(request,'wrong password or login')
            # return render(request,'users/signin.html')

    return render(request,'users/signin.html')

def signup(request):
   logout(request)
   if request.POST.get('reguser'): 
        if request.POST.get('password') == request.POST.get('passwordc'):
            User.objects.create_user(username=request.POST.get('username'),
                                    first_name = request.POST.get('name'),
                                    last_name = request.POST.get('company'),
                                    email=request.POST.get('email'),
                                    password=request.POST.get('password'))
            messages.success(request,'Account has been successfully registered')
            # return render(request,'users/signin.html')
        else:
            messages.error(request,'Account not registered,Please,try again!')                        
   return render(request,'users/signup.html')



def account_page(request):
    if request.user.username =='':
        return redirect('/signin/')
    try:
        context = {
                    'username':request.user.username,
                    'name':request.user.first_name,
                    'surname':request.user.last_name,
                    'email':request.user.email
                }
        return render(request, "users/account.html",context=context)
    except:
        return render(request, "users/account.html")



