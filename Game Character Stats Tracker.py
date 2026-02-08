class GameCharacter:
    def __init__(self, name):
        self._name = name
        self._health = 100
        self._mana = 50
        self._level = 1

    @property
    def name(self):
        return self._name

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, new_health):

        if not isinstance(new_health, int):
            raise TypeError("Health must be a integer")

        self._health = new_health
        if new_health > 100:
            self._health = 100

        if new_health < 0:
            self._health = 0

    @property
    def mana(self):
        return self._mana

    @mana.setter
    def mana(self, new_mana):

        if not isinstance(new_mana, int):
            raise TypeError("Health must be a integer")

        self._mana = new_mana

        if new_mana > 50:
            self._mana = 50

        if new_mana < 0:
            self._mana = 0

    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, new_level):
        if not isinstance(new_level, int):
            raise TypeError("Level but be a number")
        if new_level < 0:
            raise ValueError("Level must be greater than zero")
        self._level = new_level
        print(f"Level has been updated to {new_level}")

    def level_up(self):
        self._level += 1
        self.health = 100
        self.mana = 50
        print(f"{self.name} leveled up to {self.level}!")

    def __str__(self):
        return (f"Name: {self.name}\nLevel: {self.level}\nHealth: {self.health}\nMana: {self.mana}")
