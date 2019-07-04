from tkinter import *
class Registro():

        def __init__(self):
            self.dato=None
        
        def mostrar(self):
            def validar():
                pass
            ventana=Tk()
            ventana.title("Registro")
            ventana.geometry("700x590+350+50")
            ventana.resizable(width=False,height=False)
            #-------------------imagen de fondo
            icono=PhotoImage(file="../imagenes/Registro.png")
            img=Label(ventana,image=icono).pack()
            bt_register = Button(ventana, text="Registrar", fg="black", bg="#FEE780", command=validar, relief="flat", height=2,
                          width=13,font=('Arial',11)).place(x=215, y=521)
            bt_cancelar = Button(ventana, text="Cancelar", fg="black", bg="#FEE780", command=validar, relief="flat", height=2,
                          width=13,font=('Arial',11)).place(x=387, y=521)
            ventana.mainloop()

x=Registro()
x.mostrar()