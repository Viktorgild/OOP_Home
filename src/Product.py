from src.BaseProduct import BaseProduct

class LoggingMixin:
    def __init__(self, *args, **kwargs):
        class_name = self.__class__.__name__
        params = ', '.join(repr(arg) for arg in args)
        params += ', ' + ', '.join(f"{k}={v!r}" for k, v in kwargs.items())
        print(f"Создан объект класса {class_name} с параметрами: {params}")

class Product(BaseProduct, LoggingMixin):
    def __init__(self, name, description, price, quantity):
        LoggingMixin.__init__(self, name, description, price, quantity)  # Вызов конструктора миксина
        super().__init__(name, description, price, quantity)  # Вызов конструктора базового класса
        self.__price = price  # Приватный атрибут

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value <= 0:
            raise ValueError("Цена не должна быть нулевая или отрицательная")
        self.__price = value

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

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