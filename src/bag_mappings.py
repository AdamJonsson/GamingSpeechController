from time import sleep
from src.pokemon_mappings import PokemonActions
from src.helpers import Helpers
from src.keystrokes import pressReleaseKey
from src.nogba_mappings import NoGbaMappings

class BagActions:
    _numOfPotions = 3
    _numOfAntidotes = 1
    bagIsOpen = False
    awaitPokemonSelect = False

    def __init__(self, pkmnActions):
        self.pkmnActions = pkmnActions
        

    def handleBackActionForBag(self):
        if (self.awaitPokemonSelect):
            self.awaitPokemonSelect = False
            return

        self.bagIsOpen = False

    def openBag(self):
        Helpers.goBackToMainMenuState()
        pressReleaseKey(NoGbaMappings.RIGHT, sleep=0.2)
        pressReleaseKey(NoGbaMappings.A, sleep=1.5)
        pressReleaseKey(NoGbaMappings.DOWN, sleep=0.2)
        pressReleaseKey(NoGbaMappings.DOWN, sleep=0.2)
        self.bagIsOpen = True

    def usePotion(self, pokemon):
        if (self.bagIsOpen == False):
            self.openBag()
        if (self._numOfAntidotes > 0):
            pressReleaseKey(NoGbaMappings.UP, sleep=0.2)
        pressReleaseKey(NoGbaMappings.UP, sleep=0.2)
        pressReleaseKey(NoGbaMappings.A, sleep=0.2)
        pressReleaseKey(NoGbaMappings.A, sleep=0.2)

        if (pokemon != None):
            self.applyConsumableOnPokemon(pokemon)
        else:
            self.awaitPokemonSelect = True

    def useAntidote(self, pokemon):
        if (self.bagIsOpen == False):
            self.openBag()
        pressReleaseKey(NoGbaMappings.UP, sleep=0.2)
        pressReleaseKey(NoGbaMappings.A, sleep=0.2)
        pressReleaseKey(NoGbaMappings.A, sleep=0.2)

        if (pokemon != None):
            self.applyConsumableOnPokemon(pokemon)
        else:
            self.awaitPokemonSelect = True


    def applyConsumableOnPokemon(self, pokemon):
        sleep(1.5)
        self.pkmnActions.selectPkmnFromMenu(pokemon)
        sleep(3)
        Helpers.goBackToMainMenuState(backActionDelay = 1)
        self.awaitPokemonSelect = False
        self.bagIsOpen = False