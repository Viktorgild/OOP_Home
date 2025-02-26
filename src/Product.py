"""Класс для работы с товарами"""


class Product:
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price  # Приватный атрибут
        self.quantity = quantity

    @classmethod
    def new_product(cls, product_inf):
        return cls(
            name=product_inf["name"],
            price=product_inf["price"],
            description=product_inf["description"],
            quantity=product_inf["quantity"],
        )
    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price: float):
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return
        self.__price = new_price

    @property
    def list_price(self):
        return self.__price