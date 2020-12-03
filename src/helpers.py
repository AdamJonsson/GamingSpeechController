from src.nogba_mappings import NoGbaMappings
from src.keystrokes import HexKeyCodes, pressReleaseKey

class Helpers:
    def goBackToMainMenuState(numOfBackActions=3, backActionDelay=0.1):
        for _ in range(numOfBackActions):
            pressReleaseKey(NoGbaMappings.B, sleep=backActionDelay)
        pressReleaseKey(NoGbaMappings.UP, sleep=0.2)
        pressReleaseKey(NoGbaMappings.LEFT, sleep=0.2)

# Ember is on the wrong location