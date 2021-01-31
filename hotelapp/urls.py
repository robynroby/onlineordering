from django.urls import path
from . import views

urlpatterns=[
    path('', views.hotelapp, name="hotelapp"),
    path('about/', views.about, name="about"),
    path('services/', views.services, name="services"),
    path('contacts/', views.contacts, name="contacts"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    
]