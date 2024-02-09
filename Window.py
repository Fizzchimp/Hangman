from tkinter import *

class Window:
    def __init__(self, width, height):

        self.screenWidth = width
        self.screenHeight = height

        self.screen = Tk()
        self.screen.title("Hangman")
        self.screen.maxsize(1200, 800)
        self.screen["background"] = "#856ff8"

        self.screen.geometry(str(width) + "x" + str(height))

        self.imageArray = None
        self.imageLabel = None
        self.wordLabel = None

        self.currentImage = 0
        
        self.loadImages()
    
    def loadImages(self):
        self.imageArray = [PhotoImage(file = f"images/hang{i}.png") for i in range(11)]


    def setUpScreen(self, string):
        leftFrame = Frame(self.screen, width = 300, height = 800, bg = "grey")
        leftFrame.grid(row = 0, column = 0, padx = 10, pady = 5)
        rightFrame = Frame(self.screen, width = 700, height = 800, bg = "grey")
        rightFrame.grid(row = 0, column = 1, padx = 10, pady = 5, sticky = "NSEW")
