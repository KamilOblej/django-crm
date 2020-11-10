from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='dashboard'),
    path('customer/<str:pk_test>/', views.customer, name='customer'),
    path('products/', views.products, name='products'),
    path('create_order', views.create_order, name='create_order'),
]
