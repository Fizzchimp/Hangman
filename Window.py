from tkinter import *
from tkinter import messagebox
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
        self.guess = None
        
        self.loadImages()
    
    def loadImages(self):
        self.imageArray = [PhotoImage(file = f"images/hang{i}.png") for i in range(12)]


    def setUpScreen(self, string):
        leftFrame = Frame(self.screen, width = 300, height = 800, bg = "grey")
        leftFrame.grid(row = 0, column = 0, padx = 10, pady = 5)
        rightFrame = Frame(self.screen, width = 700, height = 800, bg = "grey")
        rightFrame.grid(row = 0, column = 1, padx = 10, pady = 5, sticky = "NSEW")
        
        self.imageLabel = Label(leftFrame, image = self.imageArray[self.currentImage])
        self.imageLabel.grid(row = 0, column = 0, padx = 5, pady = 5)
        
        Label(rightFrame, text = "Welcome to hangman").grid(row = 1, column = 0, padx = 5, pady = 100, sticky = "NSEW", columnspan = 11)
        self.wordLabel = Label(rightFrame, text = string, font = ("Courier", 44))
        self.wordLabel.grid(row = 2, column = 0, pady = 5, padx = 100, columnspan = 11)


        letters = [chr(65 + i) for i in range(26)]
        r = 3
        for i in range(0, 26):
            if i % 10 == 0:
                r += 1
            Button(rightFrame, text = letters[i], command = lambda i = i: self.ButtonAction(letters[i]), width = 4).grid(row = (3 + r), column = (1 + i % 10), padx = 5, pady = 5)
            

    def ButtonAction(self, string):
        self.guess = string
        
    def updateHiddenWord(self, string):
        self.wordLabel.config(text = string)
    
    def nextImage(self):
        if self.currentImage < 11:
            print("Incorrect", self.currentImage)
            self.currentImage += 1
            
            self.imageLabel.config(image = self.imageArray[self.currentImage])
            
    def endGame(self):
        messagebox.showinfo(title = "Opps you lose", message = "Im afraid you have lost")
        self.screen.destroy()

    def winGame(self):
        messagebox.showinfo(title = "Yay you win", message = "Congratulations! You have won!")
        self.screen.destroy()