from Window import *
import time

WIDTH = 1200
HEIGHT = 800

class World:
    def __init__(self):
        self.window = Window(WIDTH, HEIGHT)
        self.lives = 11
        self.word = list("COMPUTER")
        self.hiddenWord = ["_" for x in self.word]
        self.guessed = []

    def runWorld(self):
        self.window.setUpScreen(self.hiddenWord)
        self.window.screen.mainloop()

world = World()
world.runWorld()