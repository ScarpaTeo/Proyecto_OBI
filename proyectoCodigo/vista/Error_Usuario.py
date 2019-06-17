from tkinter import *
class ErrorUsuario:
    def __init__(self):
        def log():
            root.destroy()

        root = Tk()
        root.title("Error!")
        root.geometry("285x80")
        root.resizable(width=False, height=False)
        msjError = Label(root, text="Error, usuario o contraseña incorrecto", bg="red")
        msjError.place(x=22, y=10)
        Aceptar = Button(root, text="Aceptar", command=log)
        Aceptar.place(x=98, y=45)
        root.mainloop()