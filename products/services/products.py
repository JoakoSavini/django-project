from products.models import Product
from products.repositories.products import ProductRepository
from typing import List
from decimal import Decimal


class ProductService:
    
    @staticmethod
    def get_all() -> list[Product]:
        return ProductRepository.get_all() 
    
    @staticmethod
    def delete(product_id: int) -> bool:
        product = ProductRepository.get_by_id(product_id=product_id)
        if product:
            return ProductRepository.delete(product=product)
        return False
    
    @staticmethod
    def update(
        product_id: int,
        price: float,
        stock: int,
    ) -> bool:
        product = ProductRepository.get_by_id(product_id=product_id)
        if product:
            ProductRepository.update(
                product=product,
                price=price,
                stock=stock,
            )
        
    @staticmethod
    def sum_product_price(products: list[Product]) -> Decimal:
        suma = Decimal(0)
        for product in products:
            suma += product.price

        return suma