from abc import ABC, abstractmethod
from pygame_gui import UIManager
import pygame as py

class Screen(ABC):
    @abstractmethod
    def processEvents(self, event):
        pass

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def destroy(self):
        pass

class ScreenManager:
    def __init__(self, uiManager: UIManager):
        self.screens: dict[int, Screen] = {}
        self.currentScreen: Screen = None
        self.uiManager = uiManager

    def addScreen(self, id: int, screen: Screen):
        self.screens[id] = screen

    def show(self, id: int):
        if self.currentScreen:
            self.currentScreen.destroy()
        self.currentScreen = self.screens[id](self.uiManager, self)

    def processEvents(self, event: py.event.Event):
        if self.currentScreen:
            self.currentScreen.processEvents(event)

    def update(self):
        if self.currentScreen:
            self.currentScreen.update()