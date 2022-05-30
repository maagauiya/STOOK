
from http import client
import imp
from multiprocessing import context
from django.db.models import Q
import datetime
from itertools import product
from math import prod
from pydoc import cli
from random import random
from sqlite3 import Date
from statistics import quantiles
import time
from unicodedata import category
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login ,logout
# Create your views here.
from django.contrib.auth.models import User
from requests import request
from .models import *
from orders.models import *
from products.models import *
from cart.models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
def signin(request):
   

    if request.POST.get('login'):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/index/')
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


@login_required(login_url='signin')
def account_page(request):
 
    if request.POST.get('logout'):
        logout(request)
        return redirect('/signin')
   

    if request.user.username =='':
        return redirect('/')
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


@login_required(login_url='signin')
def account_info(request):
    if request.POST.get('logout'):
        logout(request)
        return redirect('/signin')
  
    if request.POST.get('name'):
        user = User.objects.get(username=request.user.username)
        user.first_name = request.POST.get('name')
        user.last_name = request.POST.get('surname')
        user.save()
        context={ 
        'name':request.POST.get('name'),
        'surname':request.POST.get('surname')
        }
        if request.POST.get('email'):
            if user.check_password(request.POST.get('password')) == True:
                user.email = request.POST.get('email')
                user.save()
                messages.success(request,'Email updated')
            else:
                messages.success(request,'Incorrect password,please try again')

        return render(request, "users/account-info.html",context)


    context={ 
        'name':request.user.first_name,
        'surname':request.user.last_name
    }

    return render(request, "users/account-info.html",context)


@login_required(login_url='signin')
def account_address(request):
    user = UserProfile.objects.get(username=request.user.username)
    context = { 
        "region" : user.region,
        "country" : user.country,
        "street" : user.street,
        "city" :   user.city,
        "postal" : user.postal_cofde,
        "apartment" :   user.apartment,
        "phone" : user.phone_number
    }
    if request.POST.get('logout'):
        logout(request)
        return redirect('/signin')

    return render(request, "users/account-address.html",context=context)

@login_required(login_url='signin')
def account_new(request):
    user = UserProfile.objects.get(username=request.user.username)

    if request.POST.get('logout'):
        logout(request)
        return redirect('/signin')
    if request.POST.get('savee'):
        user.region = request.POST.get('region')
        user.country = request.POST.get('country')
        user.city = request.POST.get('city')
        user.street = request.POST.get('street')
        user.postal_cofde = request.POST.get('postalcode')
        user.apartment = request.POST.get('apartment')
        user.phone_number = request.POST.get('phone')
        user.save()
        context = { 
        "region" : request.POST.get('region'),
        "country" : request.POST.get('country'),
        "street" : request.POST.get('street'),
        "city" : request.POST.get('city'),
        "postal" : request.POST.get('postalcode'),
        "apartment": request.POST.get('apartment'),
        "phone": request.POST.get('phone')
        }   
        return render(request, "users/account-new-address.html",context=context)


    context = { 
        "region" : user.region,
        "country" : user.country,
        "street" : user.street,
        "city" :   user.city,
        "postal" : user.postal_cofde,
        "apartment" :   user.apartment,
        "phone" : user.phone_number
    }
    return render(request, "users/account-new-address.html",context=context)


@login_required(login_url='signin')
def account_orders(request):
    # order=serializers.serialize("json",Order.objects.filter(client_id = request.user.pk))
    # print("dsdsadas",order)
    order = Order.objects.filter(client_id = request.user.pk)
    
    context = {
        "orders" : order,
        
    }

    
    return render(request, "users/account-orders.html",context=context)

@login_required(login_url='signin')
def account_news(request):
   
    return render(request, "users/account-news.html")

@login_required(login_url='signin')
def account_wishlist(request):
    cart = CartItem.objects.filter(user_id =  request.user.pk) #1,2
    total = 0

    for i in cart:
        total += int(i.total)
       
    
    context = { 
        "cart":cart,
        "total":total,
        "items": len(cart)

    }
    # if request.POST.get('buy'):
    #     item =  CartItem.objects.get(id = request.POST.get('buy') )
    #     for i in item:
    #         print(i)
    return render(request, "users/account-wishlist.html",context=context)

@login_required(login_url='signin')
def remove_from_cart(request, pk):
    cart_item = CartItem.objects.get(id=pk)
    cart_item.delete()
    return redirect('/account_wishlist')

@login_required(login_url='signin')
def order(request, pk):
    return redirect(f"/payment/{pk}")

@login_required(login_url='signin')
def order2(request,pk):
    CartItem.objects.filter(id = pk).delete()
    return redirect("/index")

@login_required(login_url='signin')
def index(request):
    
    cart = CartItem.objects.filter(user_id =  request.user.pk) #1,2
    total = 0
    
    different_products = Product.objects.filter().order_by('?')[:10]
    technologies = Product.objects.filter(category="technologies")
    furniture = Product.objects.filter(category="furniture")

    for i in cart:
  
        total += int(i.total)
    
    iq = "{% static 'users/images/cart-ico.png'%}"
    context = { 
        "cart":cart,
        "total":total,
        "items": len(cart),
        "different": different_products,
        "technologies": technologies,
        "furniture": furniture
    }
    if request.POST.get('logout'):
        logout(request)
        return redirect('/signin')
    return render(request, "users/index.html",context=context)


@login_required(login_url='signin')
def product_page(request, number):
    cart = CartItem.objects.filter(user_id =  request.user.pk) #1,2
    total = 0

    for i in cart:
  
        total += int(i.total)
    
    iq = "{% static 'users/images/cart-ico.png'%}"
    cart2=serializers.serialize("json",CartItem.objects.filter(user_id =  request.user.pk))
    product = Product.objects.get(id= number)

    print("Image", product.image)


    if request.POST.get("myForm"):
        return HttpResponse(request.POST.get("product_num"))
        # print("PRODUCT=",request.POST.get("product_num"))
        # print(request.POST.get("product_num"))
    if request.POST:
        print("8989089080980809809809")
        find_dup = CartItem.objects.filter(product=product).first()
        if find_dup != None:
            return HttpResponse("item already in the cart")
        product_num = request.POST.get('product_num')
        print(request.POST)
        
        cart_item = CartItem.objects.create(
            user = request.user,
            product = product,
            quantity = product_num,
            price = product.price,
            name = product.name,
            total = product.price*int(product_num),
            image_path = product.image.url
            
        )
        
        cart_item.save()
    context = { 
        "product": product,"cart":cart,
        "total":total,
        "items": len(cart),
        "cart2" : cart2
    }
    return render(request, "users/product.html",context=context)


@login_required(login_url='signin')
def payment(request,pk):

    cart_item = CartItem.objects.get(id = pk)
    product1 = Product.objects.get(id = cart_item.product_id)
    user = UserProfile.objects.get(user_id= request.user.pk)
    user2 = UserProfile.objects.get(user_id= product1.user_id)
    if request.POST.get("submit"):
        order = Order.objects.create(
            client = request.user,
            supplier = request.user,
            product = product1,
            quantity = cart_item.quantity,
            country = user.country,
            region = user.region,
            city = user.street,
            address = user.street,
            post_number = user.postal_cofde,
            price = cart_item.price,
            track_number = 213,
            shipping_date = datetime.datetime(2022, 5, 17),
            status = "In Process",
            total = cart_item.total ,
            name = product1.name
        )
        order.save()
        remove_from_cart(request, pk)
        return redirect("account_wishlsit")

    return render(request, "users/payment.html")



@login_required(login_url='signin')
def search(request):
    q = request.POST.get("search_field")
    products = Product.objects.filter(Q(name__icontains=q))
    cart = CartItem.objects.filter(user_id =  request.user.pk) #1,2
    total = 0

    for i in cart:
  
        total += int(i.total)
    
    context = { 
        "cart":cart,
        "total":total,
        "items": len(cart),
        "search": products
    }
    if request.POST.get('logout'):
        logout(request)
        return redirect('/signin')
    return render(request, "users/search.html", context)

@login_required(login_url='signin')
def logout_user(request):
    logout(request)
    return redirect("signin")

