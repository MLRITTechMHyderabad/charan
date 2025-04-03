class Character:
    def __init__(self, name, health, attack_power, defence, speed):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.defence = defence
        self.speed = speed

    def attack(self, target):
        damage = max(1, self.attack_power - target.defence())
        print(f"{self.name} attacks {target.name} and deals {damage} damage!")

    def take_damage(self, amount):
        self.health = self.health - amount
        print(f" {self.name} takes {amount} damage! health remaining: {self.health}")

    def is_live(self):
        return self.health > 0

class Warrior(Character):
    def __init__(self, name, health, attack_power, defence, speed):
        super().__init__(name, health, attack_power, defence, speed)
        self.rage = 0
        
