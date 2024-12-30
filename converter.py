# Python Program - English (Latin) to Hindi (Devnagiri) text convertor GUI using tkinter

# import sanscript class from the indic_transliteration module and method

from indic_transliteration import sanscript

from indic_transliteration.sanscript import transliterate

# import all functions from tkinter

from tkinter import *

# Function to clear both the text areas

def clearAll() :
    # Whole content of text area is deleted
    
    text1_field.delete(1.0, END)
    text2_field.delete(1.0, END)

# Functions to convert into Devnagiri text
def convert() :
    # get a whole input content from text box

    input_text = text1_field.get("1.0", "end")[:-1]

    output_text = transliterate(input_text, sanscript.ITRANS, sanscript.DEVANAGARI)

    text2_field.insert('end -1 chars', output_text)

# Driver Code

if __name__=="__main__":

    # Create a GUI window
    root = Tk()

    # Set the backgroundcolor of GUI window
    root.configure(background = 'light green')

    # Set the configuration of GUI window (WidthHeight)
    root.geometry("400x350")

    # set the name of tkinter GUI window
    root.title("Converter")

    # Create welcome to Latin to Devnagiri text converter
    headlebel = Label(root, text = "Welcome to Latin to Devnagiri text converter", fg = 'black', bg = 'red')

    # Create a "Latin Text" label
    label1 = Label(root, text = "Latin Text", fg = 'black', bg = 'dark green')

    # Create a "Devnagiri Text" label
    label2 = Label(root, text = "Devnagiri Text", fg = 'black', bg = 'dark green')

    headlebel.grid(row = 0, column = 1)

    # Padx keyword argument used to set padding along x-axix and Y-axis

    label1.grid(row = 1, column = 0, padx = 10, pady = 10)
    label2.grid(row = 3, column = 0, padx = 10, pady = 10)

    # create a text area
    text1_field = Text(root, height = 5, width = 25, font = "lucida 13")
    text2_field = Text(root, height = 5, width = 25, font = "lucida 13")

    text1_field.grid(row = 1, column = 1, padx = 10, pady = 10)
    text2_field.grid(row = 3, column = 1, padx = 10, pady = 10)

    # Create a convert button and attached with convert function

    button1 = Button(root, text = "Convert into devnagiri text", bg = "red", fg = "black", command = convert)
    button1.grid(row = 2, column = 1)

    # Create a Clear All button and attached with clearAll function

    button2 = Button(root, text = "Clear", bg = "red", fg = "black", command = clearAll)
    button2.grid(row = 4, column = 1)

    # start the GUI
    root.mainloop()







   