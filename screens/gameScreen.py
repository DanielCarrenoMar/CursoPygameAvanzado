from pygame_gui.elements import UIButton, UILabel
import pygame as py
import pygame_gui as pyui

from screens.ScreenManager import Screen, ScreenManager
from screens.ScreenList import ScreenList

class GameScreen(Screen):
    def __init__(self, uiManager: pyui.UIManager, screenManager: ScreenManager):
        self.screenManager = screenManager
        self.goToMainMenuButton = UIButton(relative_rect=py.Rect((400, 250), (200, 50)),
            text='Ir a Menu principal',
            manager=uiManager)
        self.titleLabel = UILabel(relative_rect=py.Rect((350, 150), (300, 50)),
            text='Página de Juego',
            manager=uiManager)

    def processEvents(self, event:py.event.Event):
        if event.type == pyui.UI_BUTTON_PRESSED and event.ui_element == self.goToMainMenuButton:
            self.screenManager.show(ScreenList.MAIN_MENU)

    def update(self):
        pass

    def destroy(self):
        self.goToMainMenuButton.kill()
        self.titleLabel.kill()