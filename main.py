import pygame as py
import pygame_gui as pyui

from screens.ScreenManager import ScreenManager, Screen
from screens.ScreenList import ScreenList
from screens.mainMenuScreen import MainMenuScreen
from screens.gameScreen import GameScreen

class App:
    def __init__(self):
        py.init()

        self.windows = py.display.set_mode((1024, 600), py.RESIZABLE)
        py.display.set_caption('Curso Pygame Avanzado')

        self.clock = py.time.Clock()
        theme = "data\\themes\\myTheme.json"
        self.manager = pyui.UIManager((1024, 600), theme)
        self.screenManager = ScreenManager(self.manager)

        self.screenManager.addScreen(ScreenList.MAIN_MENU, MainMenuScreen)
        self.screenManager.addScreen(ScreenList.GAME, GameScreen)

        self.screenManager.show(ScreenList.MAIN_MENU)
        self.running = True

    def run(self):
        while self.running:
            time_delta = self.clock.tick(60) / 1000.0

            for event in py.event.get():
                if event.type == py.QUIT:
                    self.running = False

                self.manager.process_events(event)
                self.screenManager.processEvents(event)

            self.manager.update(time_delta)
            self.screenManager.update(time_delta)
            self.windows.fill((40, 40, 40)) # Manda a rellenar toda la ventana con un color
            self.manager.draw_ui(self.windows) # Manda a dibuja los elementos de la interfaz
            self.screenManager.draw(self.windows) # Manda a dibujar la pantalla actual
            py.display.update() # Ejecuta todos los mandados

if __name__ == '__main__':
    app = App()
    app.run()
