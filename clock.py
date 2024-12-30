# Create a Digital Clock using Tkinter

# Importing whole module

from tkinter import *
from tkinter.ttk import *

# Import strftime function to retrieve system time
from time import strftime

# Createing tkinter window
root = Tk()
root.title('Clock')

# This function used to display time on the label

def time():
    string = strftime('%H:%M:%S %p')
    lbl.config(text = string)
    lbl.after(1000, time)

# styling the label widget so that clock will look more attractive

lbl = Label(root, font = ('calibri', 40, 'bold'), background = 'purple', foreground = 'white')

# Placing clock at the center of the tkinter window

lbl.pack(anchor = 'center')
time()

mainloop()


