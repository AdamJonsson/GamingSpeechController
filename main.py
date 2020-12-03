
from src.bag_mappings import BagActions
from src.pokemon_mappings import PokemonActions
from src.debug.text_input import debug_text_input
from src.microphone import microphone
from src.detect_intent import detectIntentFromSpeech
from src.intents import Intents

from src.keystrokes import pressReleaseKey
from src.nogba_mappings import NoGbaMappings

def get_microphone_stream():
    microphone.askUserForInputDevice()
    return microphone.getMicrophoneStream()

def getParameter(parameters, attr="", listValue=-1, integer=False):
    if integer: 
        return int(parameters.fields["number-integer"].list_value.values[0].number_value)
    elif listValue > -1:
        return parameters.fields[attr].list_value.values[listValue].string_value.strip()
    return parameters.fields[attr].string_value.strip()

def main():
    microphone_stream = get_microphone_stream()
    pkmnActions = PokemonActions()
    bagActions = BagActions(pkmnActions)
    while True:
        print(20 * "=")
        print("Listening for user action...")
        intent, parameters = detectIntentFromSpeech(microphone_stream)

        try: 
            if intent == Intents.GO:
                pressReleaseKey(NoGbaMappings.A)

            elif intent == Intents.BACK:
                pressReleaseKey(NoGbaMappings.B)
                bagActions.markBagAsClosed()

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
                direction =  getParameter(parameters, "Direction")
                steps = getParameter(parameters, integer=True)
                pkmnActions.walk(direction, steps)

            elif intent == Intents.FIGHT:
                print("Fight keyaction")

            elif intent == Intents.BAG:
                bagActions.openBag()

            elif intent == Intents.POTION or intent == Intents.ANTIDOTE:
                chosen = getParameter(parameters, "Pokemon")
                chosenPokemon = None
                if (chosen in pkmnActions.pkmnOrder):
                    chosenPokemon = chosen
                
                if (intent == Intents.POTION):
                    bagActions.usePotion(chosenPokemon)
                if (intent == Intents.ANTIDOTE):
                    bagActions.useAntidote(chosenPokemon)

            elif intent == Intents.SELECT_PKMN:
                chosen = getParameter(parameters, "Pokemon")
                if(chosen in pkmnActions.pkmnOrder):
                    if (bagActions.awaitPokemonSelect):
                        bagActions.applyConsumableOnPokemon(chosen)

            elif intent == Intents.CHOOSE_PKMN:
                chosen = getParameter(parameters, "Pokemon")
                if(chosen in pkmnActions.pkmnOrder):
                    pkmnActions.switchPkmn(chosen)  

            elif intent == Intents.SUMMARY:
                chosen = getParameter(parameters, "Pokemon")
                if(chosen in pkmnActions.pkmnOrder):
                    pkmnActions.viewPkmnSummary(chosen)

            elif intent == Intents.CHANGE_PAGE:
                way = getParameter(parameters, "Way")
                pkmnActions.changePage(way)

            elif intent == Intents.ATTACK:
                attack = getParameter(parameters, "Attack", listValue=0)
                pkmnActions.useAttack(attack)

            elif intent == Intents.QUIT:
                break

            else:
                print("No keyaction")
        except Exception as error:
                print(error)          

if __name__ == "__main__":
    main()