
from src.helpers import Helpers
from src.keystrokes import pressReleaseKey
from src.nogba_mappings import NoGbaMappings
from src.intents import Entities, Intents


class Pokémon:
    CHARMANDER = 'Charmander'
    SPEAROW = 'Spearow'
    CATERPIE = 'Caterpie'

class PokemonActions:
    def __init__(self): 
        self.resetPkmnOrder()
        self.disabledShortcuts = []
        self.attacks = {
            "Scratch": 0,
            "Peck": 0,
            "Tackle": 0,
            "Growl": 1,
            "String shot": 1,
            "Ember": 2,
            "Leer": 2,
            "Metal claw": 3
        }

    def resetPkmnOrder(self):
        self.pkmnOrder = [
            Pokémon.CHARMANDER,
            Pokémon.SPEAROW,
            Pokémon.CATERPIE
        ]

    def addDisabledShortcut(self, shortcut):
        if shortcut not in self.disabledShortcuts:
            self.disabledShortcuts.append(shortcut)

    def removeDisabledShortcut(self, shortcut):
        if shortcut in self.disabledShortcuts:
            self.disabledShortcuts.remove(shortcut)

    def walk(self, direction, steps):
        self.resetPkmnOrder()
        key = NoGbaMappings.UP
        if direction == Intents.UP:
            key = NoGbaMappings.UP
        elif direction == Intents.DOWN:
            key = NoGbaMappings.DOWN
        elif direction == Intents.LEFT:
            key = NoGbaMappings.LEFT
        elif direction == Intents.RIGHT:
            key = NoGbaMappings.RIGHT
        for i in range(0, steps):
            pressReleaseKey(key)

    def answerNo(self):
        pressReleaseKey(NoGbaMappings.DOWN)
        pressReleaseKey(NoGbaMappings.A)

    def selectPkmnFromMenu(self, chosen):
        chosenIndex = self.pkmnOrder.index(chosen)
        for i in range(0, chosenIndex):
            pressReleaseKey(NoGbaMappings.DOWN, sleep=0.2)
        pressReleaseKey(NoGbaMappings.A, sleep=0.2)
        return chosenIndex

    def selectPkmn(self, chosen):
        Helpers.goBackToMainMenuState()
        pressReleaseKey(NoGbaMappings.DOWN)
        pressReleaseKey(NoGbaMappings.A, sleep=1.5)
        return self.selectPkmnFromMenu(chosen)

    def switchPkmn(self, chosen):
        chosenIndex = self.selectPkmn(chosen)
        self.pkmnOrder[chosenIndex], self.pkmnOrder[0] = self.pkmnOrder[0], self.pkmnOrder[chosenIndex] 
        pressReleaseKey(NoGbaMappings.A)

    def viewPkmnSummary(self, chosen):
        self.selectPkmn(chosen)
        pressReleaseKey(NoGbaMappings.DOWN, sleep=0.2)
        pressReleaseKey(NoGbaMappings.A, sleep=0.2)
        pressReleaseKey(NoGbaMappings.A)
        self.addDisabledShortcut("next")

    def changePage(self, way):
        if way == Entities.NEXT:
            pressReleaseKey(NoGbaMappings.RIGHT)
        elif way == Entities.PREVIOUS:
            pressReleaseKey(NoGbaMappings.LEFT)

    def useAttack(self, attack):
        Helpers.goBackToMainMenuState()
        pressReleaseKey(NoGbaMappings.A, sleep=0.2)
        pressReleaseKey(NoGbaMappings.UP, sleep=0.2)
        pressReleaseKey(NoGbaMappings.LEFT, sleep=0.2)
        
        if self.attacks[attack] == 0:
            pressReleaseKey(NoGbaMappings.A)
        elif self.attacks[attack] == 1:
            pressReleaseKey(NoGbaMappings.RIGHT, sleep=0.2)
            pressReleaseKey(NoGbaMappings.A)
        elif self.attacks[attack] == 2:
            pressReleaseKey(NoGbaMappings.DOWN, sleep=0.2)
            pressReleaseKey(NoGbaMappings.A)
        elif self.attacks[attack] == 3:
            pressReleaseKey(NoGbaMappings.RIGHT, sleep=0.2)
            pressReleaseKey(NoGbaMappings.DOWN, sleep=0.2)
            pressReleaseKey(NoGbaMappings.A)

    def fight(self):
        Helpers.goBackToMainMenuState()
        pressReleaseKey(NoGbaMappings.A)

    def viewPkmn(self):
        Helpers.goBackToMainMenuState()
        pressReleaseKey(NoGbaMappings.DOWN, sleep=0.2)  
        pressReleaseKey(NoGbaMappings.A)

    def run(self):
        Helpers.goBackToMainMenuState()
        pressReleaseKey(NoGbaMappings.RIGHT, sleep=0.2)
        pressReleaseKey(NoGbaMappings.DOWN, sleep=0.2)  
        pressReleaseKey(NoGbaMappings.A)

