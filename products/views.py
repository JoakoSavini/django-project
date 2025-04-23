from django.shortcuts import render, get_object_or_404

from products.models import Product
from products.services.products import ProductService
from products.services.customers import CustomerService

def product_list(request):
    all_products = ProductService.get_all()
    suma = ProductService.sum_product_price(all_products)

    return render(
        request, 
        'products/list.html',
        dict(
            products=all_products,
            suma = suma,
            otro_atributo='Atributo 2'
        )
    )

def customer_list(request):
    all_customers = CustomerService.get_all()
    suma = CustomerService.sum_customer(all_customers)

    return render(
        request, 
        'customers/list.html',
        dict(
            customers=all_customers,
            suma = suma,
        )
    )

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(
        request,
        'products/detail.html',
        dict(
            product=product,
        )
    )

def order_list(request):
    return render(request, 'orders/list.html')