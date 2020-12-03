from src.nogba_mappings import NoGbaMappings
from src.keystrokes import HexKeyCodes, pressReleaseKey

class Helpers:
    def goBackToMainMenuState(numOfBackActions=3, backActionDelay=0.2):
        for _ in range(numOfBackActions):
            print("Menu back")
            pressReleaseKey(NoGbaMappings.B, sleep=backActionDelay)
        pressReleaseKey(NoGbaMappings.UP, sleep=0.2)
        pressReleaseKey(NoGbaMappings.LEFT, sleep=0.2)

# Ember is on the wrong location