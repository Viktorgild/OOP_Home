import pytest

from src.Category import Category
from src.Product import Product

product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)


@pytest.fixture(autouse=True)
def reset_category_count():
    """Сбрасываем счетчик категорий и продуктов перед каждым тестом."""
    Category.category_count = 0
    Category.product_count = 0  # Сбрасываем счетчик продуктов
    yield
    Category.category_count = 0  # Сбрасываем после теста
    Category.product_count = 0  # Сбрасываем после теста


@pytest.fixture()
def Product_test():
    return Product(
        name="Samsung Galaxy S23 Ultra", description="256GB, Серый цвет, 200MP камера", price=180000.0, quantity=5
    )


@pytest.fixture()
def Category_test():
    return Category(
        name="Смартфоны",
        description="Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        products=[
            Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5),
            Product("Iphone 15", "512GB, Gray space", 210000.0, 8),
            Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14),
        ],
    )
