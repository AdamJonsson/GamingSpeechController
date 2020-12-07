from tkinter import *
import ctypes

class SpeechGUI:
    BACKGROUND_COLOR = "#102040"

    def __init__(self) -> None:
        self.root = Tk()
        self.root.config(
            bg=self.BACKGROUND_COLOR,
            width=800, height=600)
        ctypes.windll.shcore.SetProcessDpiAwareness(1)

        self._currentTranscript = StringVar()
        self._currentTranscript.set("No value")
        self._currentTranscriptLabel = self._createTranscriptLabel()
        self._currentTranscriptLabel.place(relx=.5, rely=.5, anchor="center")

    def _createTranscriptLabel(self):
        return Label(
            self.root, 
            textvariable=self._currentTranscript,
            bg=self.BACKGROUND_COLOR,
            fg="#ffffff",
            font=("Algerian", 35))

    def start(self, onExitCallback):
        self.root.protocol("WM_DELETE_WINDOW", onExitCallback)
        self.root.mainloop()

    def changeText(self, newText):
        self._currentTranscript.set(newText)
    
    def quit(self):
        self.root.destroy()