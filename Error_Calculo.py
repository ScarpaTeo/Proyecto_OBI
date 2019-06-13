from tkinter import *

class ErrorCalculo:
    def __init__(self):
        self.root = Tk()
        self.root.title("Error!")
        self.root.geometry("250x80")
        self.root.resizable(width=False, height=False)
        self.msjError = Label(root, text="Error, el calculo que desea hacer es incorrecto")
        self.msjError.place(x=22, y=10)
        self.Aceptar = Button(root, text="Aceptar")
        self.Aceptar.place(x=98, y=45)
        self.root.mainloop()
