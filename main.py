
from src.debug.text_input import debug_text_input
from src.microphone import microphone
from src.detect_intent import detect_intent_from_speech
from src.intents import Intents

from src.keystrokes import pressReleaseKey
from src.nogba_mappings import NoGbaMappings

def get_microphone_stream():
    microphone.ask_user_for_input_device()
    return microphone.get_microphone_stream()

def main():
    microphone_stream = get_microphone_stream()
    while True:
        print(20 * "=")
        print("Listening for user action...")
        intent = detect_intent_from_speech(microphone_stream)

        if intent == Intents.RUN:
            print("Run keyaction")
            pressReleaseKey(NoGbaMappings.A)
        elif intent == Intents.BACK:
            print("Back keyaction")
        elif intent == Intents.FIGHT:
            print("Fight keyaction")
        elif intent == Intents.QUIT:
            break
        else:
            print("No keyaction")

if __name__ == "__main__":
    main()