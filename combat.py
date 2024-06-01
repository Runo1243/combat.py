# tbc.py
#class character
#-def init collect info
#@property def name
#def hitPoints
#@hitChance.setter def hitChance(0-100)
#@property def armor(player armor)
#print out finial message
#player vs monster
#
class Character:
    def __init__(self, name="Unknown", hitPoints=10, hitChance=50, maxDamage=5, armor=2):
        self._name = name
        self._hitPoints = hitPoints
        self._hitChance = hitChance
        self._maxDamage = maxDamage
        self._armor = armor

    def testInt(self, value, min=0, max=100, default=0):
        """ Validate that value is an int within min and max range, return default otherwise. """
        try:
            value = int(value)
            if value < min or value > max:
                raise ValueError
        except (ValueError, TypeError):
            value = default
        return value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = str(value)

    @property
    def hitPoints(self):
        return self._hitPoints

    @hitPoints.setter
    def hitPoints(self, value):
        self._hitPoints = int(value)  # No constraints as it can go negative

    @property
    def hitChance(self):
        return self._hitChance

    @hitChance.setter
    def hitChance(self, value):
        self._hitChance = self.testInt(value, 0, 100, 50)

    @property
    def maxDamage(self):
        return self._maxDamage

    @maxDamage.setter
    def maxDamage(self, value):
        self._maxDamage = self.testInt(value, 1, float('inf'), 5)

    @property
    def armor(self):
        return self._armor

    @armor.setter
    def armor(self, value):
        self._armor = self.testInt(value, 0, float('inf'), 2)

    def printStats(self):
        """ Print the character's statistics. """
        print(f"{self._name}")
        print("="*20)
        print(f"Hit points: {self._hitPoints}")
        print(f"Hit chance: {self._hitChance}")
        print(f"Max damage: {self._maxDamage}")
        print(f"Armor:      {self._armor}")

    def hit(self, opponent):
        """ Calculate a hit on the opponent. """
        import random
        hit_roll = random.randint(1, 100)
        if hit_roll <= self._hitChance:
            damage = random.randint(1, self._maxDamage)
            actual_damage = max(0, damage - opponent.armor)
            opponent.hitPoints -= actual_damage
            print(f"{self._name} hits {opponent.name} for {actual_damage} points of damage.")
            print(f"{opponent.name}'s armor absorbs {opponent.armor} points.")
        else:
            print(f"{self._name} misses {opponent.name}.")

# Main function for testing
if __name__ == "__main__":
    hero = Character("Hero", 10, 50, 5, 2)
    hero.printStats()

    monster = Character("Monster", 20, 30, 5, 0)
    monster.printStats()

    hero.hit(monster)
    monster.hit(hero)
