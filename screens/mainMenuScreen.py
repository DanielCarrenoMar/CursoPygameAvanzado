from pygame_gui.elements import UIButton, UILabel, UIImage
import pygame as py
import pygame_gui as pyui

from screens.ScreenManager import Screen, ScreenManager
from screens.ScreenList import ScreenList

class MainMenuScreen(Screen):
    def __init__(self, uiManager: pyui.UIManager, screenManager: ScreenManager):
        self.screenManager = screenManager
        self.boton_ir_acerca = UIButton(relative_rect=py.Rect((0, 100), (400, 100)),
            command=lambda: self.screenManager.show(ScreenList.GAME),
            anchors={'centerx': 'centerx', 'top': 'top'},
            text='Ir a Juego',
            manager=uiManager)
        self.tituloLabel = UILabel(
            relative_rect=py.Rect((0, 0), (300, 50)),
            text='Página de Inicio',
            anchors={'centerx': 'centerx', 'top': 'top'},
            manager=uiManager)
        self.logo_image = UIImage(
            relative_rect=py.Rect((0, 400), (200, 100)),
            image_surface=py.image.load("data\\images\\space\\space_1.jpg"),
            manager=uiManager,
            anchors={'centerx': 'centerx', 'top': 'top'}
        )

    def processEvents(self, event:py.event.Event):
        pass

    def update(self, time_delta: int):
        pass

    def draw(self, surface: py.Surface):
        pass

    def destroy(self):
        self.boton_ir_acerca.kill()
        self.tituloLabel.kill()