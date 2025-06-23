from pygame_gui.elements import UIButton, UILabel
import pygame as py
import pygame_gui as pyui
import numpy as np

from screens.ScreenManager import Screen, ScreenManager
from screens.ScreenList import ScreenList

class GameScreen(Screen):
    def __init__(self, uiManager: pyui.UIManager, screenManager: ScreenManager):
        self.screenManager = screenManager
        self.uiManager = uiManager
        self.goToMainMenuButton = UIButton(relative_rect=py.Rect((-300, 250), (300, 50)),
            anchors={"right": "right"},
            text='Ir a Menu principal',
            manager=uiManager)
        self.titleLabel = UILabel(relative_rect=py.Rect((-300, 150), (300, 50)),
            anchors={"right": "right"},
            text='Página de Juego',
            manager=uiManager)
        
        self.mat = np.zeros((3, 3), dtype=int)
        self.mat[0, 0] = 1
        self.mat[1, 1] = 2
        self.mat[2, 2] = 1
        print(self.mat)

        # Cargar imágenes para las casillas
        self.img_empty = py.image.load('data/images/space/space_1.jpg')
        self.img_1 = py.image.load('data/images/space/space_2.jpg')
        self.img_2 = py.image.load('data/images/space/space_3.jpg')
        # Redimensionar imágenes a 50x50
        self.img_empty = py.transform.scale(self.img_empty, (100, 100))
        self.img_1 = py.transform.scale(self.img_1, (100, 100))
        self.img_2 = py.transform.scale(self.img_2, (100, 100))

    def processEvents(self, event:py.event.Event):
        if event.type == pyui.UI_BUTTON_PRESSED and event.ui_element == self.goToMainMenuButton:
            self.screenManager.show(ScreenList.MAIN_MENU)

    def update(self, time_delta: int):
        pass

    def draw(self, surface: py.Surface):
        for i, row in enumerate(self.mat):
            for j, value in enumerate(row):
                x = 100 + j * 120
                y = 100 + i * 120
                if value == 0:
                    surface.blit(self.img_empty, (x, y))
                elif value == 1:
                    surface.blit(self.img_1, (x, y))
                else:
                    surface.blit(self.img_2, (x, y))

    def destroy(self):
        self.goToMainMenuButton.kill()
        self.titleLabel.kill()