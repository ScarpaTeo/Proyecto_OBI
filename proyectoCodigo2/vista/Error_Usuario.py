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
        ventana.geometry("400x85")
        ventana.resizable(width=False, height=False)
        img=PhotoImage(file="../imagenes/usuariocontraseña.png")
        msjError=Label(ventana, image=img).place(x=-2, y=-13)
        Aceptar=Button(ventana, text="Aceptar", command=Obtener)
        Aceptar.config(height=1, width=14)
        Aceptar.place(x=158, y=47.5)
        ventana.mainloop()
        return self.valor
    
    def errorCamposVacios(self):
        def Obtener():
            ventana.destroy()
            self.valor="cerrar"
        ventana = Tk()
        ventana.title("Error!")
        ventana.geometry("500x150+430+320")
        ventana.resizable(width=False, height=False)
        img=PhotoImage(file="../imagenes/campos-vacios.png")
        msjError=Label(ventana, image=img).place(x=-2, y=-13)
        Aceptar=Button(ventana, text="Aceptar", relief="flat",bg="#FFFFFF", command=Obtener)
        Aceptar.config(height=1, width=14)
        Aceptar.place(x=158, y=47.5)
        ventana.mainloop()
        return self.valor