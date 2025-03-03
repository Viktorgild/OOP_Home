"""Класс для работы с товарами"""


class Product:
    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price  # Приватный атрибут
        self.quantity = quantity

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value <= 0:
            raise ValueError("Цена не должна быть нулевая или отрицательная")
        elif hasattr(self, "_price") and value < self.__price:
            confirm = input("Вы уверены, что хотите понизить цену? (y/n): ")
            if confirm.lower() == "y":
                self.__price = value
            else:
                print("Цена не изменена.")
        else:
            self.__price = value

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __repr__(self):
        return f"{self.name}, описание: {self.description}, цена = {self.price}, количество = {self.quantity}"

    def __add__(self, other):
        if type(self) is not type(other):
            raise TypeError("Нельзя складывать продукты разных типов.")
        return (self.price * self.quantity) + (other.price * other.quantity)


class Smartphone(Product):
    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    def __init__(self, name, description, price, quantity, country, germination_period, color):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color
