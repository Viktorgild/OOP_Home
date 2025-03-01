class Category:
    name = str
    description = str
    _products = list  # Приватный атрибут

    category_count = 0
    product_count = 0

    def __init__(self, name, description, products=None):
        self.name = name
        self.description = description
        self._products = products if products is not None else []

        Category.category_count += 1
        Category.product_count += len(self._products)

    def add_product(self, product):
        self._products.append(product)
        Category.product_count += 1

    def get_product_count(self):
        return len(self._products)

    @property
    def products(self):
        return [f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт." for product in self._products]



