from products.models import Customer
from products.repositories.customers import CustomerRepository

class CustomerService:

    @staticmethod
    def get_all() -> list[Customer]:
        return CustomerRepository.get_all()
    
    @staticmethod
    def delete(customer_id: int) -> bool:
        customer = CustomerRepository.get_by_id(customer_id = customer_id)
        if customer:
            return CustomerRepository.delete(customer=customer)
        return False
    
    @staticmethod
    def update(
        customer_id: int,
        email: str,
        phone: str,
    ) -> bool:
        customer = CustomerRepository.get_by_id(customer_id = customer_id)
        if customer:
            CustomerRepository.update(
                customer = customer,
                email = email,
                phone = phone,
            )

    @staticmethod
    def sum_customer(customers: list[Customer]) -> int:
        return len(customers)