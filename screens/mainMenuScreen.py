from pygame_gui.elements import UIButton, UILabel
import pygame as py
import pygame_gui as pyui

from screens.ScreenManager import Screen, ScreenManager
from screens.ScreenList import ScreenList

class MainMenuScreen(Screen):
    def __init__(self, uiManager: pyui.UIManager, screenManager: ScreenManager):
        self.screenManager = screenManager
        self.boton_ir_acerca = UIButton(relative_rect=py.Rect((400, 250), (200, 50)),
            text='Ir a Juego',
            manager=uiManager)
        self.titulo = UILabel(relative_rect=py.Rect((350, 150), (300, 50)),
            text='Página de Inicio',
            manager=uiManager)

    def processEvents(self, event:py.event.Event):
        if event.type == pyui.UI_BUTTON_PRESSED and event.ui_element == self.boton_ir_acerca:
            self.screenManager.show(ScreenList.GAME)

    def update(self):
        pass

    def destroy(self):
        self.boton_ir_acerca.kill()
        self.titulo.kill()