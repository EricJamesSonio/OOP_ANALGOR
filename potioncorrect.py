from abc import ABC, abstractmethod


# Base Character
class NPC:
    def __init__(self, health, abilities):
        self.health = health
        self.abilities = (
            abilities  # Abilities are a list of abilities, like ["Strength", "Speed"]
        )

    def stats(self):
        return f"Health : {self.health}, Abilities : {', '.join(self.abilities)}"


# Base Potion
class Potion:
    def __init__(self):
        self.ingredients = []
        self.effects = []

    def add(self, ingredient):
        self.ingredients.append(ingredient)

    def add_effect(self, effect):
        self.effects.append(effect)

    def show(self):
        ingredients = ", ".join([ingredient.name for ingredient in self.ingredients])
        effects = ", ".join(self.effects)
        return f"Ingredients: {ingredients} | Effects: {effects}"


# Builder
class PotionBuilder(ABC):
    @abstractmethod
    def baseingredient(self, ingredient):
        pass

    @abstractmethod
    def effect(self):
        pass

    @abstractmethod
    def show(self):
        pass


class StrengthPotion(PotionBuilder):
    def __init__(self):
        self.potion = Potion()
        self.ingredient1 = Goldenhead()
        self.effect = Strength()

    def baseingredient(self):
        self.potion.add(self.ingredient1)

    def effect(self):
        self.potion.add_effect(self.effect.apply())

    def show(self):
        return self.potion.show()


class SpeedPotion(PotionBuilder):
    def __init__(self):
        self.potion = Potion()
        self.ingredient1 = Shakra()
        self.effect = Speed()

    def baseingredient(self):
        self.potion.add(self.ingredient1)

    def effect(self):
        self.potion.add_effect(self.effect.apply())

    def show(self):
        return self.potion.show()


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
        return "This is from the head of a Golem."


class Shakra(Ingredient):
    def __init__(self, name="Shakra"):
        super().__init__(name)

    def description(self):
        return "From an assassin ninja."


# Effects
class PotionEffect(ABC):
    @abstractmethod
    def apply(self):
        pass


class Strength(PotionEffect):
    def apply(self):
        return "Strength"  # Adds "Strength" effect to the potion


class Speed(PotionEffect):
    def apply(self):
        return "Speed"  # Adds "Speed" effect to the potion


# Crafting
class Craft:
    def __init__(self, builder: PotionBuilder, npc: NPC):
        self.builder = builder
        self.npc = npc

    def craft(self):
        self.builder.baseingredient()
        self.builder.effect()

    def get_potion(self):
        return self.builder.show()

    def apply_effect(self):
        for effect in self.builder.potion.effects:
            # Apply the effect to the NPC's abilities
            if effect == "Strength":
                self.npc.abilities.append("Strength")
            elif effect == "Speed":
                self.npc.abilities.append("Speed")


# Example usage
npc = NPC(health=100, abilities=["Agility"])
builder = StrengthPotion()  # You can change this to SpeedPotion for a different potion
craft = Craft(builder, npc)

craft.craft()  # Craft the potion (ingredients + effect)
craft.apply_effect()  # Apply the effect to the NPC's abilities

# Now printing the NPC's stats and crafted potion
print(npc.stats())  # NPC should have new abilities
print(craft.get_potion())  # Potion details (ingredients and effects)
