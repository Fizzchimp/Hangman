from Window import *
import time

WIDTH = 1200
HEIGHT = 800

class World:
    def __init__(self):
        self.window = Window(WIDTH, HEIGHT)
        self.lives = 11
        self.word = list("BATMAN")
        self.hiddenWord = ["_" for x in self.word]
        self.guessed = []


    def runWorld(self):
        self.window.setUpScreen(self.hiddenWord)
        self.window.screen.after(10, self.listenForGuess)
        self.window.screen.mainloop()
        

    def listenForGuess(self):
        if self.window.guess != None and self.window.guess not in self.guessed:
            self.guessed.append(self.window.guess)
            found = self.linearSearch(self.word, self.window.guess)
            
            if found != []:
                for pos in found:
                    self.hiddenWord[pos] = self.word[pos]
            else:
                self.window.nextImage()
                self.lives -= 1
                    
            self.window.updateHiddenWord(" ".join(self.hiddenWord))
            
        if self.lives == 0:
            self.window.endGame()
        if self.word == self.hiddenWord:
            self.window.winGame()
            
        self.window.screen.after(10, self.listenForGuess)
        

    def linearSearch(self, string, criteria):
        positions = []
        for i, x in enumerate(string):
            if x == criteria:
                positions.append(i)
        self.window.guess = None
        return positions

world = World()
world.runWorld()