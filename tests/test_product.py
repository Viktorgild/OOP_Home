import pytest
import unittest
from unittest.mock import patch
from io import StringIO

from src.Category import Category
from src.Order import Order
from src.Product import LawnGrass, Product, Smartphone
from src.Mixin import LoggingMixin  # Убедитесь, что вы импортируете Mixin

def test_product_creation(Product_test):
    """Тестируем создание продукта."""
    assert Product_test.name == "Samsung Galaxy S23 Ultra"
    assert Product_test.description == "256GB, Серый цвет, 200MP камера"
    assert Product_test.price == 180000.0
    assert Product_test.quantity == 5

def test_product_creation_with_zero_quantity():
    """Тестируем создание продукта с нулевым количеством."""
    with pytest.raises(ValueError, match="Товар с нулевым количеством не может быть добавлен"):
        Product(name="Test Product", description="Test", price=100.0, quantity=0)

def test_product_creation_with_negative_price():
    """Тестируем создание продукта с отрицательной ценой."""
    with pytest.raises(ValueError, match="Цена не должна быть нулевая или отрицательная"):
        Product(name="Test Product", description="Test", price=-100.0, quantity=1)

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

def test_average_price_with_no_products():
    """Тестируем среднюю цену в категории без продуктов."""
    empty_category = Category("Пустая категория", "Нет продуктов")
    assert empty_category.average_price() == 0

def test_average_price_with_products(Category_test):
    """Тестируем среднюю цену в категории с продуктами."""
    assert Category_test.average_price() == (180000.0 + 210000.0 + 31000.0) / 3

def test_order_creation():
    """Тестируем создание заказа."""
    product = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    order = Order(product, 2)
    assert order.total_price() == 360000.0  # 180000 * 2

class TestLoggingMixin(unittest.TestCase):
    @patch('sys.stdout', new_callable=StringIO)
    def test_logging_mixin_initialization(self, mock_stdout):
        # Создаем класс для тестирования, который наследует LoggingMixin
        class TestClass(LoggingMixin):
            pass

        # Создаем объект класса TestClass
        test_object = TestClass('test_name', 'test_description', price=100, quantity=5)

        # Проверяем, что вывод соответствует ожидаемому
        expected_output = "Создан объект класса TestClass с параметрами: 'test_name', 'test_description', price=100, quantity=5"
        self.assertIn(expected_output, mock_stdout.getvalue())

if __name__ == '__main__':
    unittest.main()