from abc import ABC, abstractmethod
from typing import List, Optional


class Command(ABC):
    @abstractmethod
    def execute(self):
        pass


class NPC:
    def __init__(self, health=100, strength=20, speed=15):
        self.health = health
        self.strength = strength
        self.speed = speed


class TrainStrength(Command):
    def __init__(self, npc: NPC):
        self.npc = npc

    def execute(self):
        return self.npc.strength + 10


class TrainSpeed(Command):
    def __init__(self, npc: NPC):
        self.npc = npc

    def execute(self):
        return self.npc.speed + 10


class Trainer:
    def __init__(self, command: Command):
        self.command = command

    def train(self):
        return self.command.execute()
