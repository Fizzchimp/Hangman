from Window import *
import time

WIDTH = 1200
HEIGHT = 800
class World:
    def __init__(self):
        self.window = Window(WIDTH, HEIGHT)

    def runWorld(self):
        self.window.setUpScreen("Computer")
        self.window.screen.mainloop()

world = World()
world.runWorld()
yay