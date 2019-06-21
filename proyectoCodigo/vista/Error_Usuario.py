from tkinter import *
class ErrorUsuario:
    def __init__(self):
        self.valor=None
    def mostrar(self):

        def Obtener():
            ventana.destroy()
            self.valor=True

        ventana = Tk()
        ventana.title("Error!")
        ventana.geometry("285x80")
        ventana.resizable(width=False, height=False)
        msjError = Label(ventana, text="Error, usuario o contraseña incorrecto", bg="red")
        msjError.place(x=22, y=10)
        Aceptar = Button(ventana, text="Aceptar", command=Obtener)
        Aceptar.place(x=98, y=45)
        ventana.mainloop()
        return self.valor

#x=ErrorUsuario()
#x.mostrar()
#print(x.valor)