#clase menu principal en esta deberia esta la opcion que te deja
#calcular un nuevo presupuesto
#cargar precios

from tkinter import *
from tkinter import messagebox

class MostrarMenu:
    def __init__(self):
        self.valor=False
    
    def mostrar(self):
        def cargarPr():
            ventana.destroy()
            self.valor="precios"
        #--------------------------
        def presupuesto():
            ventana.destroy()
            self.valor="presupuesto"
        #--------------------------

        def salirEscape(evento):
            pregunta = messagebox.askokcancel("Salir","¿ Desea salir de la Aplicación")
            if pregunta == True:
                ventana.destroy()

        'crea la ventana menu'
        ventana = Tk()
        ventana.title("Menu")
        ventana.geometry('700x600+350+0')
        ventana.resizable(width=False, height=False)
        ventana.bind("<Escape>",salirEscape)
        # ----------- imagen de fondo
        icono = PhotoImage(file="../imagenes/menu.png")
        Limg = Label(ventana, image=icono).pack()

        # --------------- botones nuevo presupues y cargar precio
        B_presupuesto = Button(ventana, text="Nuevo Presupuesto", fg="black", bg="#FFDE00",command=presupuesto, relief="flat", height=3,width=21,font=('Arial',13))
        B_presupuesto.place(x=139, y=360)
        B_cargarPrecio= Button(ventana, text="Cargar Precios", fg="black", bg="#FFDE00",command=cargarPr, relief="flat", height=3, width=21,font=('Arial',13))
        B_cargarPrecio.place(x=364, y=150)
        bt_ayuda = Button(ventana, text="Ayuda", fg="#FFDE00", bg="#1E1E1E", relief="flat", height=1, width=4).place(x=10, y=563)
        bt_cerrar = Button(ventana, text="Cerrar Sesión", fg="#FFDE00", bg="#2F2F2F", relief="flat", height=1, width=9).place(
            x=595, y=34)

        ventana.focus_force()
        ventana.mainloop()

#x=MostrarMenu()
#x.mostrar()
