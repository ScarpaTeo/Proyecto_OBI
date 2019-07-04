from tkinter import *
class Registro():

        def __init__(self):
            self.dato=None
        
        def mostrar(self):
            def validar():
                pass
            ventana=Tk()
            ventana.title("Registro")
            ventana.geometry("700x590+350+0")
            ventana.resizable(width=False,height=False)
            #-------------------imagen de fondo
            icono=PhotoImage(file="../imagenes/Registro.png")
            img=Label(ventana,image=icono).pack()
            bt_register = Button(ventana, text="Registrar", fg="black", bg="red", command=validar, relief="flat", height=2,
                          width=14,font=('Arial',11)).place(x=288, y=522)
            ventana.mainloop()

x=Registro()
x.mostrar()