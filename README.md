# Продуктовый менеджер

Этот проект представляет собой систему для управления товарами и их категориями. Включает классы для работы с продуктами, смартфонами и газонной травой, а также для управления категориями товаров.

## Структура проекта

Проект состоит из следующих файлов:
- `Order` Определяет классы `Order`, `BaseOrder`
- `BaseProduct.py` Определяет класс `BaseProduct`
- `product.py`: Определяет классы `Product`, `Smartphone` и `LawnGrass`.
- `category.py`: Определяет класс `Category` для работы с категориями товаров.
- `main.py`: Основной файл, который демонстрирует использование классов.
- `test.py`: Набор тестов для проверки функциональности классов с использованием библиотеки `pytest`.

## Использование

## Пример использования:
```
from src.Product import Product, Smartphone
from src.Category import Category

# Создание продуктов
product1 = Smartphone("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, "High", "S23 Ultra", "256GB", "Gray")

# Создание категории
category = Category("Смартфоны", "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни", [product1])

# Добавление нового продукта
new_product = Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, "High", "15", "512GB", "Gray")
category.add_product(new_product)

# Получение информации о категории
print(category)
```

## Установка:
1. Клонируйте репозиторий:
```
https://github.com/Viktorgild/OOP_home
```
2. Установите зависимости:
```
pip install -r requirements.txt
```

## Разработчик:

https://github.com/Viktorgild