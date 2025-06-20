from pygame_gui.elements import UIButton, UILabel, UITextEntryBox
import pygame as py
import pygame_gui as pyui
import numpy as np

from screens.ScreenManager import Screen, ScreenManager
from screens.ScreenList import ScreenList

class GameScreen(Screen):
    def __init__(self, uiManager: pyui.UIManager, screenManager: ScreenManager):
        self.screenManager = screenManager
        self.uiManager = uiManager
        self.goToMainMenuButton = UIButton(relative_rect=py.Rect((400, 250), (200, 50)),
            text='Ir a Menu principal',
            manager=uiManager)
        self.titleLabel = UILabel(relative_rect=py.Rect((350, 150), (300, 50)),
            text='Página de Juego',
            manager=uiManager)
        
        self.mat = np.zeros((3, 3), dtype=int)

    def processEvents(self, event:py.event.Event):
        if event.type == pyui.UI_BUTTON_PRESSED and event.ui_element == self.goToMainMenuButton:
            self.screenManager.show(ScreenList.MAIN_MENU)

    def update(self, time_delta: int):
        pass

    def draw(self, surface: py.Surface):
        for i, row in enumerate(self.mat):
            for j, value in enumerate(row):
                x = 100 + j * 60
                y = 100 + i * 60
                if value == 0:
                    py.draw.rect(surface, (255, 255, 255), (x, y, 50, 50))
                else:
                    py.draw.circle(surface, (0, 0, 255), (x + 25, y + 25), 20)

    def destroy(self):
        self.goToMainMenuButton.kill()
        self.titleLabel.kill()