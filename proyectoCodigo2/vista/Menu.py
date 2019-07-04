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
        ventana.focus()
        ventana.title("Menu")
        ventana.geometry('700x600+350+0')
        ventana.resizable(width=False, height=False)
        ventana.focus()
        ventana.bind("<Escape>",salirEscape)
        # ----------- imagen de fondo
        icono = PhotoImage(file="../imagenes/menu.png")
        Limg = Label(ventana, image=icono).pack()

        # --------------- botones nuevo presupues y cargar precio
        B_presupuesto = Button(ventana, text="Nuevo Presupuesto", fg="black", bg="#FFDE00",command=presupuesto, relief="flat", height=3,width=21,font=('Arial',13))
        B_presupuesto.place(x=138, y=363)
        B_cargarPrecio= Button(ventana, text="Cargar Precios", fg="black", bg="#FFDE00",command=cargarPr, relief="flat", height=3, width=21,font=('Arial',13))
        B_cargarPrecio.place(x=364, y=153)

        ventana.mainloop()