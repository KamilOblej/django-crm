from django.shortcuts import render, redirect
from django.http import HttpResponse

from . models import Product, Order, Customer
from . forms import OrderForm


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

    form = OrderForm()

    if request.method == 'POST':
        # print('Printing', request.POST)
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {
        'form': form,
    }
    return render(request, 'accounts/order_form.html', context)
