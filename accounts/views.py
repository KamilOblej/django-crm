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


def customer(request, pk_test):
    customer = Customer.objects.get(id=pk_test)
    orders = customer.order_set.all()
    orders_count = orders.count()

    context = {
        'customer': customer,
        'orders': orders,
        'orders_count': orders_count,
    }

    return render(request, 'accounts/customer.html', context)


def products(request):
    products = Product.objects.all()

    return render(request, 'accounts/products.html', {'products': products})


def create_order(request):

    context = {

    }
    return render(request, 'accounts/order_form.html', context)
