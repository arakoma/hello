from tkinter import *
from tkinter import ttk


root = Tk()
root.title("hello !")
root.geometry("256x256")

label = Label(root, text="hello !")
label.grid()

def pushed():
    print("pushed !")
button = Button(root, text="button", command=pushed)
button.grid()

root.mainloop()