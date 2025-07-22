from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def cart(request):
    return render(request, 'cart.html')

def checkout(request):
    return render(request, 'checkout.html')

def contact(request):
    return render(request, 'contact.html')

def login(request):
    return render(request, 'login.html')

def myaccount(request):
    return render(request, 'myaccount.html')

def productdetail(request):
    return render(request, 'productdetail.html')

def productlist(request):
    return render(request, 'productlist.html')

def wishlist(request):
    return render(request, 'wishlist.html')


