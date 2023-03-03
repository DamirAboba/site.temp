from django.shortcuts import render
from products.models import ProductCategory , Product

def index(request):
    return render(request , 'products/index.html' , {'title' : 'store'} )

def products(request):
    context = {
        'title' : 'Store - Каталог',
        'products' : Product.objects.all(),
        'categories': ProductCategory.objects.all(),

    }
    return render(request , 'products/products.html' , context)
