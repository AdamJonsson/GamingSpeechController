
from src.debug.text_input import debug_text_input
from src.microphone import microphone
from src.detect_intent import detect_intent_from_speech
from src.intents import Intents

from src.keystrokes import pressReleaseKey
from src.nogba_mappings import NoGbaMappings, PokemonActions

def get_microphone_stream():
    microphone.ask_user_for_input_device()
    return microphone.get_microphone_stream()

def main():
    microphone_stream = get_microphone_stream()
    while True:
        print(20 * "=")
        print("Listening for user action...")
        intent, parameters = detect_intent_from_speech(microphone_stream)
        pkmnActions = PokemonActions()

        if intent == Intents.GO:
            pressReleaseKey(NoGbaMappings.A)
        elif intent == Intents.BACK:
            pressReleaseKey(NoGbaMappings.B)
        elif intent == Intents.UP:
            pressReleaseKey(NoGbaMappings.UP)
        elif intent == Intents.DOWN:
            pressReleaseKey(NoGbaMappings.DOWN)
        elif intent == Intents.LEFT:
            pressReleaseKey(NoGbaMappings.LEFT)
        elif intent == Intents.RIGHT:
            pressReleaseKey(NoGbaMappings.RIGHT)
        elif intent == Intents.START:
            pressReleaseKey(NoGbaMappings.START)
        elif intent == Intents.NO:
            pkmnActions.answerNo()
        elif intent == Intents.DIR_N_STEPS:
            try:
                direction = parameters.fields["direction"].string_value.strip()
                steps = int(parameters.fields["number-integer"].list_value.values[0].number_value)
                pkmnActions.walk(direction, steps)
            except:
                print("error")
        elif intent == Intents.FIGHT:
            print("Fight keyaction")
        elif intent == Intents.QUIT:
            break
        else:
            print("No keyaction")

if __name__ == "__main__":
    main()