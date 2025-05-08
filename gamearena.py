from abc import ABC, abstractmethod
from typing import List, Optional


class Warrior(ABC):
    def __init__(self, attack_type, health, damage):
        self.attact_type = attack_type
        self.health = health
        self.damage = damage

    @abstractmethod
    def get_details(self):
        pass


class Knight(Warrior):
    def __init__(self, attack_type="Melee", health=200, type="Knight", damage=20):
        super().__init__(attack_type, health, damage)
        self.type = type

    def get_details(self):
        return f"Type : {self.type}, Attack type : {self.attact_type}, Health : {self.health}, Damage : {self.damage}"


class Mage(Warrior):
    def __init__(self, attack_type="Magic", health=100, type="Mage", damage=30):
        super().__init__(attack_type, health, damage)
        self.type = type

    def get_details(self):
        return f"Type : {self.type}, Attack type : {self.attact_type}, Health : {self.health}, Damage : {self.damage}"


class Archer(Warrior):
    def __init__(self, attack_type="Ranged", health=120, type="Archer", damage=25):
        super().__init__(attack_type, health, damage)
        self.type = type

    def get_details(self):
        return f"Type : {self.type}, Attack type : {self.attact_type}, Health : {self.health}, Damage : {self.damage}"


class WarriorDecorator(Warrior):
    def __init__(self, attack_type, health, damage, warrior: Warrior):
        super().__init__(attack_type, health, damage)
        self._warrior = warrior

    @abstractmethod
    def get_details(self):
        pass

    @abstractmethod
    def damage_power(self):
        return self.damage


class FireSword(WarriorDecorator):

    def get_details(self):
        return self._warrior.get_details() + " + FireSword (Equipped)"

    def damage_power(self):
        return self._warrior.damage() + 25


class IceArrow(WarriorDecorator):

    def get_details(self):
        return self._warrior.get_details() + " + IceArrow (Equipped)"

    def damage_power(self):
        return self._warrior.damage() + 30


class MagicStaff(WarriorDecorator):

    def get_details(self):
        return self._warrior.get_details() + " + MagicStaff (Equipped)"

    def damage_power(self):
        return self._warrior.damage() + 50


class AttackStrategy(ABC):
    def __init__(self, warrior: Warrior):
        self.warrior = warrior

    @abstractmethod
    def attack(self):
        pass


class MeleeAttack(AttackStrategy):
    def attack(self):
        return self.warrior.damage


class RangedAttack(AttackStrategy):
    def attack(self):
        return self.warrior.damage


class MagicAttack(AttackStrategy):
    def attack(self):
        return self.warrior.damage


class WarriorFactory:
    def create(self, warrior_type):
        if warrior_type == "Knight":
            return Knight()
        elif warrior_type == "Archer":
            return Archer()
        elif warrior_type == "Mage":
            return Mage()


builder = WarriorFactory()
k1 = builder.create("Knight")
print(k1.get_details())
