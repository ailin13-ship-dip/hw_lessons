class Hero:
    def __init__(self,name,health,power):
        self.name = name
        self.health = health
        self.power = power

    def action(self):
        print(f"{self.name} совершает базовое действие.")
