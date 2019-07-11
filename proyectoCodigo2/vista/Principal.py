from tkinter import *
from animaciones import *
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
        def Reporte():
            ventana.destroy()
            self.dato="reporte"
        def animacion():
            pass
        

        Bcimiento=Button(ventana, text="Cimiento",fg="black",activebackground="#FFDE00", bg="#FFDE00",relief="flat", height=2, width=27, font=("Arial",13),command=cimiento)
        Bcimiento.place(x=299, y=93)

        Bpared=Button(ventana, text="Pared",fg="black",activebackground="#FFDE00",bg="#FFDE00",relief="flat", height=2, width=27, font=("Arial",13),command=pared)
        Bpared.place(x=299,y=193)

        Bcontrapiso=Button(ventana, text="Contrapiso",fg="black",activebackground="#FFDE00",bg="#FFDE00",relief="flat", height=2, width=27, font=("Arial",13),command=contrapiso)
        Bcontrapiso.place(x=299, y=296)

        Brevoque=Button(ventana, text="Revoque",fg="black",activebackground="#FFDE00",bg="#FFDE00",relief="flat", height=2, width=27, font=("Arial",13),command=revoque)
        Brevoque.place(x=299, y=399)

        Btecho=Button(ventana, text="Techo",fg="black",activebackground="#FFDE00", bg="#FFDE00",relief="flat", height=2, width=27, font=("Arial",13),command=techo)
        Btecho.place(x=299, y=500)
        # ---------boton atras
        Batras=Button(ventana,width=8,relief="flat",activebackground="#303030",bg="#303030",fg="#FFDE00",font=('Arial',10),text="Atras",command=volverAtras).place(x=598,y=24)
        
        Bimprimir=Button(ventana,width=8,relief="flat",activebackground="#292929",bg="#292929",fg="#FFDE00",font=('Arial',10),text="Imprimir",command=Reporte).place(x=503,y=24)

        bt_ayuda = Button(ventana, text="Ayuda",command=animacion, fg="#FFDE00",activebackground="#1E1E1E", bg="#1E1E1E", relief="flat", height=1, width=4).place(x=10, y=563)
        ventana.focus_force()
        ventana.mainloop()
        return self.dato
#x=Principal()
#x.mostrar()