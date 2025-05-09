from django.urls import path

from products.views import (
    CustomerList,
    ProductCreateView,
    ProductDelete,
    ProductDetail,
    ProductList,
    OrderList, 
)

urlpatterns = [
    path(
        route='create_product/', 
        view=ProductCreateView.as_view(), 
        name='product_create'
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
        route='product_delete/<int:product_id>/',
        view=ProductDelete.as_view(),
        name='product_delete'
    ),
    path(
        route='order_list/', 
        view=OrderList.as_view(), 
        name='order_list'
    ),
    path(
        route='customer_list/',
        view=CustomerList.as_view(),
        name='customer_list'
    )
]