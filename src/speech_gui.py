import time
from tkinter import *
import ctypes
from types import new_class

from six import b

class SpeechGUI:
    BACKGROUND_COLOR = "#004000"
    INACTIVE_BACKGROUND_COLOR = "#555555"
   

    def __init__(self) -> None:
        self._lastCommand = "None"

        self.root = Tk()
        self.root.config(
            bg=self.BACKGROUND_COLOR,
            width=800, height=600)
        ctypes.windll.shcore.SetProcessDpiAwareness(1)

        self.centerFrame = self._createCenterFrame()
        
        self._currentHistoryLabel = self._createAndPlaceHistoryLabel(self.centerFrame)
        self._currentHistoryText = self._createAndPlaceHistoryText(self.centerFrame)

        Frame(self.centerFrame, bg="#ffffff", height=2).pack(fill="x", pady=25)

        self._currentTranscriptLabel = self._createAndPlaceTranscriptLabel(self.centerFrame)
        self._currentTranscriptText = self._createAndPlaceTranscriptText(self.centerFrame)


    def _createCenterFrame(self):
        centerFrame = Frame(self.root, bg=self.BACKGROUND_COLOR)
        centerFrame.place(           
            relx=.5, 
            rely=.5, 
            anchor="center"
        )
        return centerFrame


    def _createAndPlaceHistoryLabel(self, centerFrame: Frame):
        newLabel = Label(
            centerFrame, 
            text="Last command",
            bg=self.BACKGROUND_COLOR,
            fg="#cccccc",
            font=("Berlin Sans FB", 25)
        )
        newLabel.pack()
        return newLabel

    def _createAndPlaceHistoryText(self, centerFrame: Frame):
        newLabel = Label(
            centerFrame, 
            text="None",
            bg=self.BACKGROUND_COLOR,
            fg="#cccccc",
            font=("Berlin Sans FB", 35)
        )
        newLabel.pack()
        return newLabel

    def _createAndPlaceTranscriptLabel(self, centerFrame: Frame):
        newLabel = Label(
            centerFrame, 
            text="Listening",
            bg=self.BACKGROUND_COLOR,
            fg="#cccccc",
            font=("Berlin Sans FB", 25)
        )
        newLabel.pack()
        return newLabel

    def _createAndPlaceTranscriptText(self, centerFrame: Frame):
        newLabel = Label(
            centerFrame, 
            text="...",
            bg=self.BACKGROUND_COLOR,
            fg="#ffffff",
            font=("Berlin Sans FB", 35)
        )
        newLabel.pack()
        return newLabel

    def toggleExecutingCommandView(self, on: bool):
        newBackgroundColor = self.BACKGROUND_COLOR
        if on:
            newBackgroundColor = self.INACTIVE_BACKGROUND_COLOR
            self._currentTranscriptLabel.config(text="Executing command")
        else:
            self._currentTranscriptLabel.config(text="Listening")

        self._changeBackgroundColor(newBackgroundColor)

    def showNoIntentFoundStatus(self):
        self._changeBackgroundColor("#800000")
        self._currentTranscriptLabel.config(text="Couldn't find command")
        time.sleep(2)

    def _changeBackgroundColor(self,newBackgroundColor):
        self.root.config(bg=newBackgroundColor)
        self.centerFrame.config(bg=newBackgroundColor)
        self._currentTranscriptLabel.config(bg=newBackgroundColor)
        self._currentTranscriptText.config(bg=newBackgroundColor)
        self._currentHistoryText.config(bg=newBackgroundColor)
        self._currentHistoryLabel.config(bg=newBackgroundColor)

    def start(self, onExitCallback):
        self.root.protocol("WM_DELETE_WINDOW", onExitCallback)
        self.root.mainloop()

    def updateHistoryText(self):
        self._currentHistoryText.config(text=self._lastCommand)
        self.changeText("")

    def changeText(self, newText):
        if newText != "":
            self._lastCommand = newText
        
        if newText == "":
            newText = "..."
            
        self._currentTranscriptText.config(text=newText)
    
    def quit(self):
        self.root.destroy()