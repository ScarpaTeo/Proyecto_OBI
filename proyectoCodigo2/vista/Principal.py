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

        Bcimiento=Button(ventana, text="Cimiento",fg="black", bg="#FFDE00",relief="flat", height=2, width=25, font=("Arial",12),command=cimiento)
        Bcimiento.place(x=259, y=106)

        Bpared=Button(ventana, text="Pared",fg="black", bg="#FFDE00",relief="flat", height=2, width=25, font=("Arial",12),command=pared)
        Bpared.place(x=259,y=198)

        Bcontrapiso=Button(ventana, text="Contrapiso",fg="black", bg="#FFDE00",relief="flat", height=2, width=25, font=("Arial",12),command=contrapiso)
        Bcontrapiso.place(x=259, y=288)

        Brevoque=Button(ventana, text="Revoque",fg="black", bg="#FFDE00",relief="flat", height=2, width=25, font=("Arial",12),command=revoque)
        Brevoque.place(x=259, y=380)

        Btecho=Button(ventana, text="Techo",fg="black", bg="#FFDE00",relief="flat", height=2, width=25, font=("Arial",12),command=techo)
        Btecho.place(x=259, y=475)
        # ---------boton atras
        Batras=Button(ventana,width=8,relief="flat",bg="#303030",fg="#FFDE00",font=('Arial',10),text="Atras",command=volverAtras).place(x=598,y=37)
        Bimprimir=Button(ventana,width=8,relief="flat",bg="#292929",fg="#FFDE00",font=('Arial',10),text="Imprimir",command=volverAtras).place(x=503,y=37)

        bt_ayuda = Button(ventana, text="Ayuda", fg="#FFDE00", bg="#1E1E1E", relief="flat", height=1, width=4).place(x=10, y=563)
        ventana.focus_force()
        ventana.mainloop()
        return self.dato

#x=Principal()
#x.mostrar()