class Product:
    """
    Класс для описания товара в магазине
    """
    name: str
    description: str
    price: float
    quantity: int

    @classmethod
    def new_product(cls, ):
        return cls.name, cls.price, cls.quantity, cls.description

    def __init__(self, name, description, price, quantity, product):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
        self.product = product

@property
def price(self):
    return self.__price
@price.setter
def price(self, __price):
    if self.__price <=0:
        print('Цена не должна быть нулевая или отрицательная')

class Category:
    """
    Класс для категорий товара
    """
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products

    def add_product(self, product: Product):
        self.__products.append(product)

        Category.category_count += 1
        Category.product_count += len(self.__products)

    @property
    def products(self):
        for product in self.__products:
            return f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт."
