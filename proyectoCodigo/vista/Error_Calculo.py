from tkinter import *

class Error_Calculo():
    def __init__(self):
        self.valor=""
    def errorValoresIncorrectos(self):
        def des():
            root.destroy()
            self.valor="cerrar"
        root = Tk()
        root.title("Error!")
        root.geometry("260x80")
        root.resizable(width=False, height=False)
        msjError = Label(root, text="Error, Ingrese VALORES correcto ",bg="red")
        msjError.place(x=22, y=10)
        Aceptar = Button(root, text="Aceptar",command=des)
        Aceptar.place(x=93, y=45)
        root.mainloop()
        return self.valor
    
    def errorCamposVacios(self):
        def des():
            root.destroy()
            self.valor="cerrar"
        root = Tk()
        root.title("Error!")
        root.geometry("260x80")
        root.resizable(width=False, height=False)
        msjError = Label(root, text="Error, Todos los campos deben estar completos",bg="red")
        msjError.place(x=22, y=10)
        Aceptar = Button(root, text="Aceptar",command=des)
        Aceptar.place(x=93, y=45)
        root.mainloop()
        return self.valor
