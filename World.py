from Window import *
import time

WIDTH = 800
HEIGHT = 650
class World:
    def __init__(self):
        self.window = Window(WIDTH, HEIGHT)

    def runWorld(self):
        #self.window.SetUpScreen("Computer")
        print(self.window.screenWidth)
        self.window.screen.mainloop()

world = World()
world.runWorld()