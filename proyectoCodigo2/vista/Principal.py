from tkinter import *
class Principal():

    def __init__(self):
        self.dato=None


    def mostrar(self):
        ventana=Tk()
        ventana.title("Principal")
        ventana.geometry('700x600+350+0')
        ventana.resizable(width=False,height=False)
        #----------- imagen de fondo
        icono=PhotoImage(file="../imagenes/Opc.png")
        Limg=Label(ventana,image=icono).pack()

        
        def cimiento():
            ventana.destroy()
            self.dato="cimiento"

        def pared():
            ventana.destroy()
            self.dato="pared"

        def contrapiso():
            ventana.destroy()
            self.dato="contrapiso"

        def revoque():
            ventana.destroy()
            self.dato="revoque"

        def techo():
            ventana.destroy()
            self.dato="techo"

        def volverAtras():
            ventana.destroy()
            self.dato="menu"

        Bcimiento=Button(ventana, text="Cimiento",fg="black", bg="#FFDE00",relief="flat", height=2, width=33, font=("Arial",12),command=cimiento)
        Bcimiento.place(x=205, y=142)

        Bpared=Button(ventana, text="Pared",fg="black", bg="#FFDE00",relief="flat", height=2, width=33, font=("Arial",12),command=pared)
        Bpared.place(x=205,y=219)

        Bcontrapiso=Button(ventana, text="Contrapiso",fg="black", bg="#FFDE00",relief="flat", height=2, width=33, font=("Arial",12),command=contrapiso)
        Bcontrapiso.place(x=205, y=295)

        Brevoque=Button(ventana, text="Revoque",fg="black", bg="#FFDE00",relief="flat", height=2, width=33, font=("Arial",12),command=revoque)
        Brevoque.place(x=205, y=373)

        Btecho=Button(ventana, text="Techo",fg="black", bg="#FFDE00",relief="flat", height=2, width=33, font=("Arial",12),command=techo)
        Btecho.place(x=205, y=450)
        # ---------boton atras
        Batras=Button(ventana,width=8,relief="flat",bg="#FFFFFF",font=('Arial',10),text="Atras",command=volverAtras).place(x=518,y=80)

        ventana.mainloop()
        return self.dato

#x=Principal()
#x.mostrar()