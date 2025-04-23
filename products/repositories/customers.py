from products.models import Customer

class CustomerRepository:
    """ 
    clase que maneja los customer/usuarios
    """

    """ crear customer """
    @staticmethod
    def create(
        name=str, 
        email=str, 
        phone=str) -> Customer:

        return Customer.objects.create(
        name = name,
        email = email,
        phone = phone
    )


    """ eliminar customer  """
    @staticmethod
    def delete (customer: Customer) -> bool:

        try: 
            customer.delete()
        except:
            raise ValueError("Error al eliminar customer")
        
    
    """ editar producto """
    @staticmethod
    def update(
        customer: Customer, 
        email: str, 
        phone: str) -> Customer:

        customer.email = email
        customer.phone = phone
        customer.save()

        return 
    
#-----------------/-----------------/-----------------/-----------------/

    @staticmethod
    def get_all() -> list[Customer]:
        """ 
        buscar todos los customer 
        """

        return Customer.objects.all()
    

    @staticmethod
    def get_by_id(customer_id: int) -> list[Customer]:
        """ 
        buscar por id
        """

        try:
            return Customer.objects.get(id=customer_id)
        except Customer.DoesNotExist:
            return None

    
    @staticmethod
    def search_by_name(name: str) -> list[Customer]:
        """ 
        buscar customer por nombre
        """

        return Customer.objects.filter(name_icontains=name)
        #los names que contengan esa cadena

