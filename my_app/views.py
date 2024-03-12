from django.shortcuts import render
from .models import Product

def product_list(request):
    products = Product.objects.all()
    return render(request, 'my_app/product_list.html', {'products': products})

def product_detail(request, product_id):
    product = Product.objects.get(id=product_id)
    return render(request, 'my_app/product_detail.html', {'product': product})

from django.shortcuts import render

def customer_home(request):
    customer_name = "John Doe"
    context = {
        'customer_name': customer_name
    }
    return render(request, 'customer_home.html', context)