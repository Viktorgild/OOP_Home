import pytest
from src.Category import Category
from src.Product import Product, Smartphone, LawnGrass
from src.Order import Order

def test_product_creation(Product_test):
    """Тестируем создание продукта."""
    assert Product_test.name == "Samsung Galaxy S23 Ultra"
    assert Product_test.description == "256GB, Серый цвет, 200MP камера"
    assert Product_test.price == 180000.0
    assert Product_test.quantity == 5

def test_category_creation(Category_test):
    """Тестируем создание категории."""
    assert Category_test.name == "Смартфоны"
    assert (
        Category_test.description
        == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    )
    assert len(Category_test.products) == 3

def test_add_product_to_category(Category_test):
    """Тестируем добавление продукта в категорию."""
    new_product = Smartphone("Nokia 3310", "Классический телефон", 5000.0, 10, "Low", "3310", "16MB", "Black")
    Category_test.add_product(new_product)
    assert len(Category_test.products) == 4

def test_product_count_in_category(Category_test):
    """Тестируем количество продуктов в категории."""
    assert Category_test.get_product_count() == 3

def test_category_product_count(Category_test):
    """Тестируем общее количество продуктов в категориях."""
    assert Category.category_count == 1  # Убедитесь, что категория была создана
    assert Category.product_count == 3  # Проверяем количество продуктов в категории

def test_product_price_setter(Product_test):
    """Тестируем сеттер для цены продукта."""
    Product_test.price = 200000.0
    assert Product_test.price == 200000.0

    # Проверка на отрицательную цену
    with pytest.raises(ValueError, match="Цена не должна быть нулевая или отрицательная"):
        Product_test.price = -100.0

def test_product_str(Product_test):
    """Тестируем строковое отображение продукта."""
    assert str(Product_test) == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."

def test_category_str(Category_test):
    """Тестируем строковое отображение категории."""
    assert str(Category_test) == "Смартфоны, количество продуктов: 27 шт."

def test_order_creation():
    """Тестируем создание заказа."""
    product = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    order = Order(product, 2)
    assert order.total_price() == 360000.0  # 180000 * 2
