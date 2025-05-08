from abc import ABC, abstractmethod
from typing import List, Optional


# Base Character
class NPC:
    def __init__(self, health, abilities):
        self.health = health
        self.abilities = abilities

    def stats(self):
        return f"Health : {self.health}, Ability : {self.abilities}"


# Base Potion
class Potion:
    def __init__(self):
        self.ingredients = []

    def add(self, ingredients):
        self.ingredients.append(ingredients)

    def show(self):
        return ", ".join(self.ingredients)


# Builder
class PotionBuilder(ABC):
    @abstractmethod
    def baseingredient(self, ingredient):
        pass

    @abstractmethod
    def show(self):
        pass


class StrengthPotion(PotionBuilder):
    def __init__(self):
        self.potion = Potion()
        self.effects = PotionEffect(Strength)
        self.ingredient1 = Goldenhead()

    def baseingredient(self):
        self.potion.ingredients.append(self.ingredient1)

    def effect(self):
        return self.effect.effect()

    def show(self):
        return self.potion()


class SpeedPotion(PotionBuilder):
    def __init__(self):
        self.potion = Potion()
        self.effects = PotionEffect(Speed)
        self.ingredient1 = Shakra()

    def baseingredient(self):
        self.potion.ingredients.append(self.ingredient1)

    def effect(self):
        return self.effect.effect()

    def show(self):
        return self.potion()


# Ingredients
class Ingredient(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def description(self):
        pass


class Goldenhead(Ingredient):
    def __init__(self, name="Golden head"):
        super().__init__(name)

    def description(self):
        return "This is From the head of a Golemn"


class Shakra(Ingredient):
    def __init__(self, name="Shakra"):
        super().__init__(name)

    def description(self):
        return "From a assasin ninja"


# Effects
class PotionEffect(ABC):
    def __init__(self, effect=None):
        self.npc = NPC()
        self.effect = effect

    @abstractmethod
    def effect(self):
        return self.npc.abilities == self.effect


class Strength(PotionEffect):
    def __init__(self, effect="Strength"):
        self.npc = NPC()
        self.effect = effect

    @abstractmethod
    def effect(self):
        return self.npc.abilities == self.effect


class Speed(ABC):
    def __init__(self, effect="Speed"):
        self.npc = NPC()
        self.effect = effect

    @abstractmethod
    def effect(self):
        return self.npc.abilities == self.effect


# Crafting
class Craft:
    def __init__(self, builder: PotionBuilder):
        self.potion = builder

    def craft(self):
        self.potion.baseingredient()


builder = StrengthPotion()
craft = Craft(builder)

craft.craft()

print(potion=builder.show())
