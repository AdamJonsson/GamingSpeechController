
import time
from src.speech_gui import SpeechGUI
from src.bag_mappings import BagActions
from src.pokemon_mappings import PokemonActions
from src.debug.text_input import debug_text_input
from src.microphone import microphone
from src.detect_intent import detectIntentFromSpeech
from src.intents import Intents

from src.keystrokes import pressReleaseKey
from src.nogba_mappings import NoGbaMappings

import tkinter as tk
from threading import Thread 

class GamingSpeechController:

    def __init__(self) -> None:
        self.pkmnActions = PokemonActions()
        self.bagActions = BagActions(self.pkmnActions)
        self.microphoneStream = self._getMicrophoneStream()
        self._quitRequest = False;

    def quit(self):
        self._quitRequest = True
        self.speechGUI.quit()

    def start(self):
        self.speechGUI = SpeechGUI()
        self.control_thread = Thread(target=self._checkForIntent, daemon=True)
        self.control_thread.start()
        self.speechGUI.start(onExitCallback=self.quit)
        self.control_thread.join()

    def _getMicrophoneStream(self):
        microphone.askUserForInputDevice()
        return microphone.getMicrophoneStream()

    def _getParameter(self, parameters, attr="", listValue=-1, integer=False):
        if integer: 
            return int(parameters.fields["number-integer"].list_value.values[0].number_value)
        elif listValue > -1:
            return parameters.fields[attr].list_value.values[listValue].string_value.strip()
        return parameters.fields[attr].string_value.strip()

    def _checkForIntent(self):
        if self._quitRequest:
            return

        print(20 * "=")
        print("Listening for user action...")
        intent, parameters = detectIntentFromSpeech(self.microphoneStream, self.speechGUI, self.pkmnActions.disabledShortcuts)

        self.speechGUI.updateHistoryText()
        if intent != Intents.UNKNOWN:
            self.speechGUI.toggleExecutingCommandView(on=True)
        else:
            self.speechGUI.showNoIntentFoundStatus()

        try: 
            if intent == Intents.GO:
                pressReleaseKey(NoGbaMappings.A)
                self.pkmnActions.removeDisabledShortcut("next")

            elif intent == Intents.BACK:
                pressReleaseKey(NoGbaMappings.B)
                self.pkmnActions.removeDisabledShortcut("next")
                self.bagActions.handleBackActionForBag()

            elif intent == Intents.UP:
                pressReleaseKey(NoGbaMappings.UP)

            elif intent == Intents.DOWN:
                pressReleaseKey(NoGbaMappings.DOWN)

            elif intent == Intents.LEFT:
                pressReleaseKey(NoGbaMappings.LEFT)

            elif intent == Intents.RIGHT:
                pressReleaseKey(NoGbaMappings.RIGHT)

            elif intent == Intents.NO:
                self.pkmnActions.answerNo()

            elif intent == Intents.DIR_N_STEPS:
                direction =  self._getParameter(parameters, "Direction")
                steps = self._getParameter(parameters, integer=True)
                self.pkmnActions.walk(direction, steps)

            elif intent == Intents.FIGHT:
                self.pkmnActions.fight()

            elif intent == Intents.BAG:
                self.bagActions.openBag()

            elif intent == Intents.POKEMON:
                self.pkmnActions.viewPkmn()

            elif intent == Intents.RUN:
                self.pkmnActions.run()

            elif intent == Intents.POTION or intent == Intents.ANTIDOTE:
                chosen = self._getParameter(parameters, "Pokemon")
                chosenPokemon = None
                if (chosen in self.pkmnActions.pkmnOrder):
                    chosenPokemon = chosen
                
                if (intent == Intents.POTION):
                    self.bagActions.usePotion(chosenPokemon)
                if (intent == Intents.ANTIDOTE):
                    self.bagActions.useAntidote(chosenPokemon)

            elif intent == Intents.SELECT_PKMN:
                chosen = self._getParameter(parameters, "Pokemon")
                if(chosen in self.pkmnActions.pkmnOrder):
                    if (self.bagActions.awaitPokemonSelect):
                        self.bagActions.applyConsumableOnPokemon(chosen)

            elif intent == Intents.CHOOSE_PKMN:
                chosen = self._getParameter(parameters, "Pokemon")
                if(chosen in self.pkmnActions.pkmnOrder):
                    self.pkmnActions.switchPkmn(chosen)  

            elif intent == Intents.SUMMARY:
                chosen = self._getParameter(parameters, "Pokemon")
                if(chosen in self.pkmnActions.pkmnOrder):
                    self.pkmnActions.viewPkmnSummary(chosen)

            elif intent == Intents.CHANGE_PAGE:
                way = self._getParameter(parameters, "Way")
                self.pkmnActions.changePage(way)

            elif intent == Intents.ATTACK:
                attack = self._getParameter(parameters, "Attack", listValue=0)
                self.pkmnActions.useAttack(attack)

            elif intent == Intents.QUIT:
                return;

            else:
                print("No keyaction")
        except Exception as error:
                print(error)     

        self.speechGUI.toggleExecutingCommandView(on=False)
        self._checkForIntent();  


def main():
    gamingSpeechController = GamingSpeechController()
    gamingSpeechController.start()
           

if __name__ == "__main__":
    main()