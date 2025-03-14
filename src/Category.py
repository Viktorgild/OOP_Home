from src.Product import LawnGrass, Product, Smartphone


class Category:
    name: str
    description: str
    _products: list  # Приватный атрибут

    category_count = 0
    product_count = 0

    def __init__(self, name, description, products=None):
        self.name = name
        self.description = description
        self._products = products if products is not None else []

        Category.category_count += 1
        Category.product_count += len(self._products)

    def add_product(self, product):
        if not isinstance(product, (Product, Smartphone, LawnGrass)):
            raise TypeError("Можно добавлять только продукты, смартфоны или траву газонную.")
        self._products.append(product)
        Category.product_count += 1

    def get_product_count(self):
        return len(self._products)

    @property
    def products(self):
        return [str(product) for product in self._products]

    def average_price(self):
        try:
            total_price = sum(product.price for product in self._products)
            return total_price / len(self._products)
        except ZeroDivisionError:
            return 0

    def __str__(self):
        total_quantity = sum(product.quantity for product in self._products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."
