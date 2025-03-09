from src.Product import LawnGrass, Product, Smartphone

class Category:
    name = str
    description = str
    __products = list  # Приватный атрибут

    category_count = 0
    product_count = 0

    def __init__(self, name, description, products=None):
        self.name = name
        self.description = description
        self.__products = products if products is not None else []

        Category.category_count += 1
        Category.product_count += len(self.__products)

    def add_product(self, product):
        if not isinstance(product, (Product, Smartphone, LawnGrass)):
            raise TypeError("Можно добавлять только продукты, смартфоны или траву газонную.")
        self.__products.append(product)
        Category.product_count += 1

    def get_product_count(self):
        return len(self.__products)

    @property
    def products(self):
        return [str(product) for product in self.__products]

    def __str__(self):
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."