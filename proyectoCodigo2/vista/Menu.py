#clase menu principal en esta deberia esta la opcion que te deja
#calcular un nuevo presupuesto
#cargar precios

from tkinter import *

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
        'crea la ventana menu'
        ventana = Tk()
        ventana.title("Menu")
        ventana.geometry('700x600+350+0')
        ventana.resizable(width=False, height=False)

        # ----------- imagen de fondo
        icono = PhotoImage(file="../imagenes/menu.png")
        Limg = Label(ventana, image=icono).pack()

        # --------------- botones nuevo presupues y cargar precio
        B_presupuesto = Button(ventana, text="Nuevo Presupuesto", fg="black", bg="#FFDE00",command=presupuesto, relief="flat", height=3,width=21,font=('Arial',13))
        B_presupuesto.place(x=138, y=363)
        B_cargarPrecio= Button(ventana, text="Cargar Precios", fg="black", bg="#FFDE00",command=cargarPr, relief="flat", height=3, width=21,font=('Arial',13))
        B_cargarPrecio.place(x=364, y=153)

        ventana.mainloop()

#x=MostrarMenu()
#x.mostrar()