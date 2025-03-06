from abc import ABC, abstractmethod

class BaseOrder(ABC):
    @abstractmethod
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity

    @abstractmethod
    def total_price(self):
        pass

class Order(BaseOrder):
    def __init__(self, product, quantity):
        super().__init__(product, quantity)

    def total_price(self):
        return self.product.price * self.quantity