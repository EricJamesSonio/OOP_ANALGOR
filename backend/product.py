class ProductItem:
    def __init__(self, name, id, size, price, quantity):
        self.name = name
        self.id = id
        self.price = price
        self.quantity = quantity
        self.size = size

    def get_details(self):
        return f"Name : {self.name}, Id : {self.id}, Price : {self.price}, Quantity : {self.quantity}"


class Coffee(ProductItem):
    def __init__(self, name, id, size, price, quantity, flavor):
        super().__init__(
            name,
            id,
            size,
            price,
            quantity,
        )
        self.flavor = flavor


class MilkCoffee(Coffee):
    pass


class ChocolateCoffee(Coffee):
    pass


class Dessert(ProductItem):
    def __init__(self, name, id, size, price, quantity):
        super().__init__(name, id, size, price, quantity)


class LecheFlan(Dessert):
    pass


class CreamCheese(Dessert):
    pass
