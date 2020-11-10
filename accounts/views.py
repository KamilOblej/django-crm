from django.shortcuts import render
from django.http import HttpResponse

from . models import Product, Order, Customer


def home(request):
    oreders = Order.objects.all()
    customers = Customer.objects.all()

    total_customers = customers.count()

    total_orders = oreders.count()
    delivered = oreders.filter(status='Delivered').count()
    pending = oreders.filter(status='Pending').count()

    context = {
        'orders': oreders,
        'customers': customers,
        'total_customers': total_customers,
        'total_orders': total_orders,
        'delivered': delivered,
        'pending': pending,
    }
    return render(request, 'accounts/dashboard.html', context)


def customer(request):
    return render(request, 'accounts/customer.html')


def products(request):
    products = Product.objects.all()

    return render(request, 'accounts/products.html', {'products': products})
