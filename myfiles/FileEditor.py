from tkinter import *
from tkinter.filedialog import asksaveasfilename
from tkinter.filedialog import askopenfilename

class FileEditor:
    def __init__(self):
        window = Tk()
        window.title("Simple Text Editor")
        
        # create a menu bar
        menubar = Menu(window)
        window.config(menu = menubar) # Display the menu bar
        
        # Create a pull-down menu and add it to the menu bar
        operationMenu = Menu(menubar, tearoff = 0)
        menubar.add_cascade(label = "File", menu = operationMenu)
        
        operationMenu.add_command(label = "Open", command = self.openFile)
        operationMenu.add_command(label = "Save", command = self.saveFIle)
        
        # Add a tool bar frame
        frame0 = Frame(window) # Create and add a frame to window
        frame0.grid(row = 1, column = 1, sticky = W)
        
        # Create images
        openImage = PhotoImage(file = "image/open.gif")
        saveImage = PhotoImage(file = "image/save.gi")