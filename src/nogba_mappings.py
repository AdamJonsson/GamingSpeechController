from src.keystrokes import HexKeyCodes, pressReleaseKey
from src.intents import Intents

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

class PokemonActions:
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