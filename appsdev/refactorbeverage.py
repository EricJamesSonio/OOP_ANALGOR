from baseproduct import *

# ------------------------- Beverage --------------------------- #

class Beverage(ProductBase):
    def __init__(self, name, code, price, supplier, quantity, unit, expiration_date):
        super().__init__(name, code, price, supplier, quantity, unit, expiration_date)


# ------------------------- Local Beverage (e.g., local desserts, juices) --------------------------- #

class LocalBeverage(Beverage):
    pass


# ------------------------- Local Juices --------------------------- #

class LocalJuice(LocalBeverage):
    pass


class CalamansiJuice(LocalJuice):
    pass


# ------------------------- Drinks (Softdrinks, Juices, Water, Tea, Shakes) --------------------------- #

class Drink(Beverage):
    pass


# Soft Drinks

class SoftDrink(Drink):
    pass


class SpriteZero(SoftDrink):
    pass


class Sprite1LT(SoftDrink):
    pass


class Coke1LT(SoftDrink):
    pass


# Juices

class Juice(Drink):
    pass


class OrangeJuice(Juice):
    pass


class BukoJuice(Juice):
    pass


# Water

class Water(Drink):
    pass


# Tea Drinks

class TeaDrink(Drink):
    pass


class IcedTea(TeaDrink):
    pass


# Shakes

class Shake(Drink):
    pass


class MangoShake(Shake):
    pass


# ------------------------- Local Desserts --------------------------- #

class LocalDessert(LocalBeverage):
    pass


class LechePlan(LocalDessert):
    pass


class HaloHalo(LocalDessert):
    pass
