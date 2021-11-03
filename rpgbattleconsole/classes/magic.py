import random


# magics abilities
class Spell:
    def __init__(self, name, cost, dmg, spellType):
        self.name = name
        self.cost = cost
        self.dmg = dmg
        self.type = spellType

    # generate random damage due to magic spell
    def generate_damage(self):
        mgl = self.dmg - 15
        mgh = self.dmg + 15
        return random.randrange(mgl, mgh)