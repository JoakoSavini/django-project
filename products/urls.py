from django.urls import path

from products.views import (
    order_list, 
    product_detail,
    product_list,  # no se usan mas
    customer_list,
    product_create,
    ProductList,
    ProductDetail,
)

urlpatterns = [
    path(
        route='create_product/', 
        view=product_create, 
        name='create_product'
    ),
    path(
        route='product_list/', 
        view=ProductList.as_view(), 
        name='product_list'
    ),
    path(
        route='product_detail/<int:product_id>/',
        view=ProductDetail.as_view(),
        name='product_detail'
    ),
    path(
        route='order_list/', 
        view=order_list, 
        name='order_list'
    ),
    path(
        route='customer_list/',
        view=customer_list,
        name='customer_list'
    )
]