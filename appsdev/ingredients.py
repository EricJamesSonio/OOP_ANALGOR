from baseproduct import *


class Ingredients(ProductBase):
    def __init__(self, name, code, price, supplier, quantity, unit, expiration_date):
        super().__init__(name, code, price, supplier, quantity, unit, expiration_date)


# ------------------------- Meat --------------------------- #


class Meat(Ingredients):
    def __init__(self, name, code, price, supplier, quantity, unit, expiration_date):
        super().__init__(name, code, price, supplier, quantity, unit, expiration_date)


class ChickenWings(Meat):
    pass


class Bacon(Meat):
    pass


# ------------------------- Spices --------------------------- #


class Spices(Ingredients):
    def __init__(self, name, code, price, supplier, quantity, unit, expiration_date):
        super().__init__(name, code, price, supplier, quantity, unit, expiration_date)


class LemonPepper(Spices):
    pass


class Seasonings(Spices):
    pass


class Salt(Spices):
    pass


# ------------------------- DryGoods --------------------------- #


class DryGoods(Ingredients):
    def __init__(self, name, code, price, supplier, quantity, unit, expiration_date):
        super().__init__(name, code, price, supplier, quantity, unit, expiration_date)


class Flour(DryGoods):
    pass


# ------------------------- CookingOil --------------------------- #


class CookingOil(Ingredients):
    def __init__(self, name, code, price, supplier, quantity, unit, expiration_date):
        super().__init__(name, code, price, supplier, quantity, unit, expiration_date)


class Oil(CookingOil):
    pass


# ------------------------- Vegetables --------------------------- #


class Vegetables(Ingredients):
    def __init__(self, name, code, price, supplier, quantity, unit, expiration_date):
        super().__init__(name, code, price, supplier, quantity, unit, expiration_date)


class Potatoes(Vegetables):
    pass


# ------------------------- Dairy --------------------------- #


class Dairy(Ingredients):
    def __init__(self, name, code, price, supplier, quantity, unit, expiration_date):
        super().__init__(name, code, price, supplier, quantity, unit, expiration_date)


class Cheese(Dairy):
    pass
