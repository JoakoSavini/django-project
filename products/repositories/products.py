from products.models import Product

class ProductRepository:
    """ 
    clase que se encarga de conectarse con la db para
    manipular productos 
    """

    """ crear prod """
    @staticmethod
    def create(
        name: str, 
        price: float, 
        stock: int
        ) -> Product:

        return Product.objects.create(
            name=name, 
            price=price, 
            stock=stock
            )

    """ eliminar prod """
    @staticmethod
    def delete(product: Product) -> bool:

        try: 
            product.delete()
        except:
            raise ValueError("No se ha podido eliminar el producto")
        

    """ editar prod """
    @staticmethod
    def update (product: Product, price: float, stock: int) -> Product:

        product.price = price
        product.stock = stock
        product.save()

        return product


#-----------------/-----------------/-----------------/-----------------/

    """ obtener todos los prod """
    @staticmethod
    def get_all() -> list[Product]:

        return Product.objects.all()
    

    """ obtener los prod por id """
    @staticmethod
    def get_by_id(product_id: int) -> list[Product]:
        
        """ para que no explote si no encuentra nada """
        try:
            return Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return None 
    
    """ obtener todos los prod por name """
    @staticmethod
    def search_by_name(name: str) -> list[Product]:

        return Product.objects.filter(name_icontains=name)
        ############################# atributo --> que contenga esta cadena

    
    """ obtengo los productos por precio """
    @staticmethod
    def search_by_price(min_price: float, max_price: float) -> list[Product]:
        
        #este para buscar en rangos delimitados (entre X y X)
        return Product.objects.filter(price_range = (min_price, max_price))

        #este para buscar menor a y mayor a     
        #return Product.objects.filter(price__gte=min_price, price__lte=max_price)