from abc import ABC, abstractmethod

# Шаг 1: Создание абстрактного класса Room
class Room(ABC):
    def __init__(self, features, price):
        self._features = features  # одно подчеркивание для хранения списка удобств
        self.__price = price       # два подчеркивания для хранения цены номера

    @abstractmethod
    def get_price(self):
        return self.__price

    @abstractmethod
    def get_features(self):
        return self._features

# Шаг 2: Создание классов для номеров
class StandardRoom(Room):
    def get_price(self):
        return self._Room__price

    def get_features(self):
        return self._features

class LuxuryRoom(Room):
    def get_price(self):
        return self._Room__price

    def get_features(self):
        features = self._features.copy()
        features.append(self.get_wifi_description())
        features.append(self.get_breakfast_description())
        return features

class FamilyRoom(Room):
    def get_price(self):
        return self._Room__price

    def get_features(self):
        features = self._features.copy()
        features.append(self.get_wifi_description())
        return features

# Шаг 3: Создание классов дополнительных услуг
class WiFiService:
    def get_wifi_description(self):
        return "Free Wi-Fi"

class BreakfastService:
    def get_breakfast_description(self):
        return "Free breakfast included"

# Шаг 4: Применение множественного наследования
class LuxuryRoom(Room, WiFiService, BreakfastService):
    def get_price(self):
        return self._Room__price

    def get_features(self):
        features = self._features.copy()
        features.append(self.get_wifi_description())
        features.append(self.get_breakfast_description())
        return features

class FamilyRoom(Room, WiFiService):
    def get_price(self):
        return self._Room__price

    def get_features(self):
        features = self._features.copy()
        features.append(self.get_wifi_description())
        return features

# Шаг 4.3: Создание экземпляров и вывод данных
standard_room = StandardRoom(features=["TV", "Mini Bar"], price=100)
luxury_room = LuxuryRoom(features=["TV", "Mini Bar", "Air Conditioner"], price=200)
family_room = FamilyRoom(features=["TV", "Mini Bar", "Play Area"], price=150)

rooms = [standard_room, luxury_room, family_room]

for room in rooms:
    print(f"{room.__class__.__name__}: Price = {room.get_price()}, Features = {room.get_features()}")