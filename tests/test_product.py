import pytest
from src.Category import Category
from src.Product import Product


# Предполагается, что Product уже определен в src/Product.py

@pytest.fixture(autouse=True)
def reset_category_counts():
    """Сброс счетчиков категорий и продуктов перед каждым тестом."""
    Category.category_count = 0
    Category.product_count = 0


@pytest.fixture()
def product1():
    return Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)


@pytest.fixture()
def product2():
    return Product("Iphone 15", "512GB, Gray space", 210000.0, 8)


@pytest.fixture()
def product3():
    return Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)


@pytest.fixture()
def category_with_products(product1, product2, product3):
    return Category(
        name="Смартфоны",
        description="Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        products=[product1, product2, product3],
    )


def test_category_initialization(category_with_products):
    category = category_with_products
    assert category.name == "Смартфоны"
    assert category.description == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    assert len(category._products) == 3
    assert Category.category_count == 1
    assert Category.product_count == 3


def test_add_product(category_with_products):
    new_product = Product("Google Pixel 7", "128GB, Black", 60000.0, 10)
    category_with_products.add_product(new_product)

    assert len(category_with_products._products) == 4
    assert Category.product_count == 4  # Проверяем, что количество продуктов увеличилось на 1
    assert new_product in category_with_products._products  # Проверяем, что новый продукт добавлен


def test_products_property(category_with_products):
    expected_output = (
        "Название продукта: Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.\n"
        "Название продукта: Iphone 15, 210000.0 руб. Остаток: 8 шт.\n"
        "Название продукта: Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт.\n"
    )
    assert category_with_products.products == expected_output


def test_category_count():
    initial_count = Category.category_count
    new_category = Category("Лaptops", "Различные ноутбуки")
    assert Category.category_count == initial_count + 1


def test_product_count():
    initial_product_count = Category.product_count
    new_category = Category("Tablets", "Различные планшеты", products=[Product("iPad Pro", "12.9-inch", 80000.0, 3)])
    assert Category.product_count == initial_product_count + 1