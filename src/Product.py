"""Класс для работы с товарами"""


class Product:
    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self._price = price  # Приватный атрибут
        self.quantity = quantity

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value <= 0:
            raise ValueError("Цена не должна быть нулевая или отрицательная")  # Выбрасываем исключение
        elif hasattr(self, "_price") and value < self._price:
            confirm = input("Вы уверены, что хотите понизить цену? (y/n): ")
            if confirm.lower() == "y":
                self._price = value
            else:
                print("Цена не изменена.")
        else:
            self._price = value

    def __str__(self):
        return self.name  # Возвращаем название товара

    def __repr__(self):
        return f"{self.name}, описание: {self.description}, цена = {self.price}, количество = {self.quantity}"
