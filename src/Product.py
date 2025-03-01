class Product:
    name = str
    description = str
    price = int
    quantity = int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


    def __str__(self):
        return self.name  # Возвращаем название товара


    def __repr__(self):
        return f'{self.name}, описание: {self.description}, цена = {self.price}, количество ={self.quantity}'