from django.contrib import messages

from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView, 
    ListView, 
)
from django.urls import reverse_lazy

from products.models import Customer, Product, Order
from products.services.products import ProductService
from products.services.customers import CustomerService
from products.forms import ProductForms


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

class ProductCreateView(CreateView):
    form_class = ProductForms
    template_name = 'products/create_product.html'
    success_url = reverse_lazy('product_list')

    def form_valid(self, form):
        messages.success(self.request, "Producto Creado")
        return super().form_valid(form)

class CustomerList(ListView):
    model = Customer 
    template_name = 'customers/list.html'
    context_object_name = 'customers'

class ProductDetail(DetailView):
    model = Product
    template_name = 'products/detail.html'
    context_object_name = 'product'
    pk_url_kwarg = 'product_id' # Nombre con el que va a encontrar el ID en la URL


class ProductDelete(DeleteView):
    model = Product
    template_name = "products/delete.html"
    pk_url_kwarg = 'product_id'
    success_url = reverse_lazy('product_list') # Nombre con el que va a encontrar el ID en la URL

class OrderList(ListView):
    model = Order
    template_name = 'orders/list.html'
    context_object_name = 'orders'

