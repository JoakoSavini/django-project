from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, ListView

from products.models import Product
from products.services.products import ProductService
from products.services.customers import CustomerService

from django.contrib import messages

# Vista basada en clases
class ProductList(ListView):
    model = Product
    template_name = 'products/list.html'
    context_object_name = 'products'

class ProductDetail(DetailView):
    model = Product
    template_name = 'products/detail.html'
    context_object_name = 'products'
    pk_url_kwarg = 'product_id'


def product_create(request):
    if request.method == 'POST':
        data = request.POST
        name = data.get('name')
        price = data.get('price')
        stock = data.get('stock')
        
        if not name or not price or not stock:
            messages.error(request, "Faltan datos")
        
        elif Product.objects.filter(name=name).exists():
            messages.error(request, "El producto ya está cargado")


        else:
            Product.objects.create(
                name=name,
                price=price,
                stock=stock,
            )
        
        

    """ aca el method es GET """
    return render(
        request,
        'products/create_product.html',
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

# DEPRECADO
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