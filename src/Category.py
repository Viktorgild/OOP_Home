class Category:
    name: str
    description: str
    _products: list  # Используем одно подчеркивание для защищенного атрибута
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products=None):
        self.name = name
        self.description = description
        self._products = products if products is not None else []  # Инициализация пустым списком
        Category.category_count += 1
        Category.product_count += len(self._products)

    @property
    def products(self):
        products_str = ""
        for product in self._products:
            products_str += f"Название продукта: {product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
        return products_str

    def add_product(self, product):
        """Добавление продукта"""
        self._products.append(product)
        Category.product_count += 1  # Увеличиваем только количество продуктов
