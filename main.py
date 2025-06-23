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

        self.clock = py.time.Clock() # Creamos el reloj para controlar el tiempo
        theme = "data\\themes\\myTheme.json" # Ubicacion del tema
        self.manager = pyui.UIManager((1024, 600), theme) # Creamos el administrador de la interfaz de usuario
        self.screenManager = ScreenManager(self.manager) # Creamos el administrador de pantallas

        self.screenManager.addScreen(ScreenList.MAIN_MENU, MainMenuScreen) # Agregamos la pantalla del menu principal
        # Para agregar una pantalla se le pasa un int que sera su id y una clase para que el administrador la maneje
        self.screenManager.addScreen(ScreenList.GAME, GameScreen)

        self.screenManager.show(ScreenList.MAIN_MENU) # Mostramos la pantalla del menu principal al iniciar
        self.running = True # Variable para controlar el bucle principal de la aplicacion

    def run(self):
        while self.running:
            time_delta = self.clock.tick(60) / 1000.0 # Controlamos el tiempo entre frames, 60 FPS

            for event in py.event.get():
                if event.type == py.QUIT:
                    self.running = False

                self.manager.process_events(event) # Procesa los eventos de la interfaz de usuario
                self.screenManager.processEvents(event) # Procesa los eventos de la pantalla actual

            self.manager.update(time_delta) # Actualiza la interfaz de usuario
            self.screenManager.update(time_delta) # Actualiza la pantalla actual
            self.windows.fill((40, 40, 40)) # Manda a rellenar toda la ventana con un color
            self.manager.draw_ui(self.windows) # Manda a dibuja los elementos de la interfaz
            self.screenManager.draw(self.windows) # Manda a dibujar la pantalla actual
            py.display.update() # Ejecuta todos los mandados

if __name__ == '__main__':
    app = App()
    app.run()
