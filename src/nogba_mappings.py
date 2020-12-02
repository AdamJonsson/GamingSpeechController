from src.keystrokes import HexKeyCodes, pressReleaseKey
from src.intents import Intents, Entities

class NoGbaMappings:
    UP = HexKeyCodes.Q
    DOWN = HexKeyCodes.A
    LEFT = HexKeyCodes.O
    RIGHT = HexKeyCodes.P
    A = HexKeyCodes.SPACE
    B = HexKeyCodes.TAB
    SELECT = HexKeyCodes.CTRL
    START = HexKeyCodes.ENTER
    L = HexKeyCodes.ALT
    R = HexKeyCodes.RIGHT_ALT
    X = HexKeyCodes.X
    Y = HexKeyCodes.Z

class Pokémon:
    CHARMANDER = 'Charmander'
    SPEAROW = 'Spearow'
    CATERPIE = 'Caterpie'

class AttackIndex:
    SCRATCH = 0
    PECK = 0
    TACKLE = 0
    GROWL = 1
    STRING_SHOT = 1
    EMBER = 1
    LEER = 2
    METAL_CLAW = 3

class PokemonActions:
    def __init__(self): 
        self.pkmnOrder = [
            Pokémon.CHARMANDER,
            Pokémon.SPEAROW,
            Pokémon.CATERPIE
        ]
        self.attacks = {
            "Scratch": 0,
            "Peck": 0,
            "Tackle": 0,
            "Growl": 1,
            "String shot": 1,
            "Ember": 1,
            "Leer": 2,
            "Metal claw": 3
        }

    def walk(self, direction, steps):
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

    def selectPkmn(self, chosen):
        #TODO Add Adam's "go_to_main_menu_state" function
        pressReleaseKey(NoGbaMappings.DOWN)
        pressReleaseKey(NoGbaMappings.A, sleep=1.5)
        chosenIndex = self.pkmnOrder.index(chosen)
        for i in range(0, chosenIndex):
            pressReleaseKey(NoGbaMappings.DOWN, sleep=0.2)
        pressReleaseKey(NoGbaMappings.A, sleep=0.2)
        return chosenIndex

    def switchPkmn(self, chosen):
        chosenIndex = self.selectPkmn(chosen)
        self.pkmnOrder[chosenIndex], self.pkmnOrder[0] = self.pkmnOrder[0], self.pkmnOrder[chosenIndex] 
        pressReleaseKey(NoGbaMappings.A)

    def viewPkmnSummary(self, chosen):
        self.selectPkmn(chosen)
        pressReleaseKey(NoGbaMappings.DOWN, sleep=0.2)
        pressReleaseKey(NoGbaMappings.A, sleep=0.2)
        pressReleaseKey(NoGbaMappings.A)

    def changePage(self, way):
        if way == Entities.NEXT:
            pressReleaseKey(NoGbaMappings.RIGHT)
        elif way == Entities.PREVIOUS:
            pressReleaseKey(NoGbaMappings.LEFT)

    def useAttack(self, attack):
        #TODO Add Adam's "go_to_main_menu_state" function
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




