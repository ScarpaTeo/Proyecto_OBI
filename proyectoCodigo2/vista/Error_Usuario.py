from tkinter import *
class Error_Usuario():
    def __init__(self):
        self.valor=""
    def errorUsarioIncorrecto(self):
        def Obtener():
            ventana.destroy()
            self.valor="cerrar"
        ventana = Tk()
        ventana.title("Error!")
        ventana.geometry("285x80+550-450")
        ventana.resizable(width=False, height=False)
        msjError = Label(ventana, text="Error, usuario o contraseña incorrecto", bg="red")
        msjError.place(x=22, y=10)
        Aceptar = Button(ventana, text="Aceptar", command=Obtener)
        Aceptar.place(x=98, y=45)
        ventana.mainloop()
        return self.valor
    
    def errorCamposVacios(self):
        def Obtener():
            ventana.destroy()
            self.valor="cerrar"
        ventana = Tk()
        ventana.title("Error!")
        ventana.geometry("285x80+550-450")
        ventana.resizable(width=False, height=False)
        msjError = Label(ventana, text="Error, Todos los campos deben estar copletos", bg="red")
        msjError.place(x=22, y=10)
        Aceptar = Button(ventana, text="Aceptar", command=Obtener)
        Aceptar.place(x=98, y=45)
        ventana.mainloop()
        return self.valor