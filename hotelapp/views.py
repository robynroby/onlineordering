from django.shortcuts import render
from .models import *
# Create your views here.


def hotelapp (request):
    products = Product.objects.all()
    context ={'products':products}
    return render(request, 'hotelapp/index.html', context)



def about (request):
    context ={}
    return render(request, 'hotelapp/about.html', context)


def services (request):
    context ={}
    return render(request, 'hotelapp/services.html', context)


def contacts (request):
    context ={}
    return render(request, 'hotelapp/contacts.html', context)

def cart (request):
    context ={}
    return render(request, 'hotelapp/cart.html', context)

def checkout (request):
    context ={}
    return render(request, 'hotelapp/checkout.html', context)
