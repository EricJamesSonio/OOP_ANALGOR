class Base:
    def __init__(self, name, code, price, quantity, category=None):
        self.name = name
        self.code = code
        self.price = price
        self.quantity = quantity
        self.category = category

    def __str__(self):
        return self.name

    def get_details(self):
        return f"[{self.index}] Name : {self.name}, Id : {self.code}, Price : {self.price}, Quantity : {self.quantity}, Category : {self.category}"


# ------------------------ Food ----------------------- #


class Food(Base):
    pass


# ------------------------ Main Course ----------------------- #


class MainCourse(Food):
    pass


class FriedChicken(MainCourse):
    pass


class PorkBarbeque(MainCourse):
    pass


# ------------------------ Dessert ----------------------- #


class Dessert(Food):
    pass


class IceCream(Dessert):
    pass


class Milktea(Dessert):
    pass


# ------------------------ Ingredients ----------------------- #


class Ingredients(Base):
    def __init__(self, name, id, price, quantity, category, supplier):
        super().__init__(name, id, price, quantity, category)
        self.supplier = supplier


# ------------------------ Poulty ----------------------- #


class Poulty(Ingredients):
    pass


class Chicken(Poulty):
    pass


class Pork(Poulty):
    pass


# ------------------------ Condiments ----------------------- #


class Condiments(Ingredients):
    pass


class Cream(Condiments):
    pass


class Flavor(Condiments):
    pass
