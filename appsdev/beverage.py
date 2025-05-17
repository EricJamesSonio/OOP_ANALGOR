from baseproduct import *

# ------------------------- Beverage --------------------------- #


class Beverage(ProductBase):
    def __init__(self, name, code, price, supplier, quantity, unit, expiration_date):
        super().__init__(name, code, price, supplier, quantity, unit, expiration_date)


# ------------------------- Local Beverage --------------------------- #


class LocalBeverage(Beverage):
    def __init__(self, name, code, price, supplier, quantity, unit, expiration_date):
        super().__init__(name, code, price, supplier, quantity, unit, expiration_date)


# ------------------------- Local Drinks  --------------------------- #


class LocalDrinks(LocalBeverage):
    pass


# ------------------------- Local Juice  --------------------------- #


class LocalJuice(LocalDrinks):
    pass


class CalamansiJuice(LocalDrinks):
    pass


# ------------------------- Drinks --------------------------- #


class Drinks(Beverage):
    pass


# ------------------------- Softdrinks --------------------------- #


class SoftDrinks(Drinks):
    pass


# ------------------------- SoftdrinksAssorted --------------------------- #


class SoftdrinksAssorted(SoftDrinks):
    pass


class SpriteZero(SoftdrinksAssorted):
    pass


class Sprite1LT(SoftdrinksAssorted):
    pass


class Coke1LT(SoftdrinksAssorted):
    pass


# ------------------------- Juice --------------------------- #


class Juice(Drinks):
    pass


class OrangeJuice(Juice):
    pass


class BukoJuice(Juice):
    pass


# ------------------------- Water --------------------------- #


class Water(Drinks):
    pass


# ------------------------- Tea Drinks --------------------------- #


class TeaDrinks(Drinks):
    pass


class IcedTea(TeaDrinks):
    pass


# ------------------------- Shakes --------------------------- #


class Shake(Drinks):
    pass


class MangoShake(Shake):
    pass


# ------------------------- Dessert --------------------------- #


class LocalDessert(LocalBeverage):
    pass


class LechePlan(LocalDessert):
    pass


class HaloHalo(LocalDessert):
    pass
