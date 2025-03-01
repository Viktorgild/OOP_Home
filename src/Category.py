class Category:
    name = str
    description = str
    products = str

    category_count = 0
    product_count = 0

    def __init__(self, name, description, products=None):
        self.name = name
        self.description = description
        self.products = products if products is not None else []

        # Увеличиваем общее количество категорий
        Category.category_count += 1

        # Увеличиваем общее количество товаров
        Category.product_count += len(self.products)

    def add_product(self, product):
        self.products.append(product)
        # Увеличиваем общее количество товаров
        Category.product_count += 1

    def get_product_count(self):
        return len(self.products)

    def get_product_names(self):
        return [product.name for product in self.products]




