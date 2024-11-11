from lessons.main import Hero

class IchigoKurosaki(Hero):
    def __init__(self,name,health,power,spiritual_energy):
        super().__init__(name, health , power)
        self.spiritual_energy = spiritual_energy

    def action(self):
        super().action()
        print(f"{self.name} активирует свою способность: Банкай!")
        self.spiritual_energy -= 10

    def use_bankai(self):
        if self.spiritual_energy > 0:
            print(f"{self.name} использует Банкай! Оставшаяся духовная энергия: {self.spiritual_energy}")
            self.spiritual_energy -= 10
        else:
            print(f"{self.name} не может использовать Банкай, духовная энергия на исходе.")

ichigo = IchigoKurosaki(name="Ичиго Куросаки", health=100, power=50, spiritual_energy=30)

ichigo.action()
ichigo.use_bankai()
ichigo.use_bankai()
ichigo.use_bankai()

