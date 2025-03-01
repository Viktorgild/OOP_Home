import pytest
from src.Product import Product
from src.Category import Category

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
        name="Samsung Galaxy S23 Ultra",
        description="256GB, Серый цвет, 200MP камера",
        price=180000.0,
        quantity=5
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

def test_product_creation(Product_test):
    """Тестируем создание продукта."""
    assert Product_test.name == "Samsung Galaxy S23 Ultra"
    assert Product_test.description == "256GB, Серый цвет, 200MP камера"
    assert Product_test.price == 180000.0
    assert Product_test.quantity == 5

def test_category_creation(Category_test):
    """Тестируем создание категории."""
    assert Category_test.name == "Смартфоны"
    assert Category_test.description == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    assert len(Category_test.products) == 3

def test_add_product_to_category(Category_test):
    """Тестируем добавление продукта в категорию."""
    new_product = Product("Nokia 3310", "Классический телефон", 5000.0, 10)
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

def test_product_price_change_confirmation(Product_test, monkeypatch):
    """Тестируем логику подтверждения изменения цены."""
    Product_test.price = 200000.0  # Устанавливаем новую цену

    # Имитация ввода 'n' для отмены изменения цены
    monkeypatch.setattr('builtins.input', lambda _: 'n')
    Product_test.price = 150000.0  # Пытаемся понизить цену
    assert Product_test.price == 200000.0  # Цена не должна измениться

    # Имитация ввода 'y' для подтверждения изменения цены
    monkeypatch.setattr('builtins.input', lambda _: 'y')
    Product_test.price = 150000.0  # Пытаемся понизить цену
    assert Product_test.price == 150000.0  # Цена должна измениться