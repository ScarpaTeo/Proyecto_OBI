from tkinter import *
class Error_Usuario():
    def __init__(self):
        self.valor=""


    def errorUsarioIncorrecto(self):
        def Obtener():
            ventana.destroy()
            self.valor="cerrar"
        
        def pressEnter(evento): 
            Obtener()

        ventana = Tk()
        ventana.title('ERROR')
        ventana.geometry('570x110+430+320')
        ventana.bind("<Return>",pressEnter)
        img = PhotoImage(file="../imagenes/usuariocontraseña.png")
        Licono = Label(ventana, image=img).pack()
        msjError=Label(ventana, image=img).place(x=-2, y=-13)
        Aceptar=Button(ventana, text="Aceptar", relief="flat",bg="#FFD42A", command=Obtener)
        Aceptar.config(height=2, width=20)
        Aceptar.place(x=211, y=61)
        ventana.focus_force()
        ventana.mainloop()
        return self.valor
    
    def errorCamposVacios(self):
        def Obtener():
            ventana.destroy()
            self.valor="cerrar"
        
        def pressEnter(evento): 
            Obtener()

        ventana = Tk()
        ventana.title("Error!")
        ventana.geometry("570x110+430+320")
        ventana.bind("<Return>",pressEnter)
        ventana.resizable(width=False, height=False)
        img=PhotoImage(file="../imagenes/campos-vacios.png")
        msjError=Label(ventana, image=img).place(x=-2, y=-13)
        Aceptar=Button(ventana, text="Aceptar", relief="flat",bg="#FFD42A", command=Obtener)
        Aceptar.config(height=2, width=20)
        Aceptar.place(x=211, y=61)
        ventana.focus_force()
        ventana.mainloop()
        return self.valor
