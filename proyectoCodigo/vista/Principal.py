from tkinter import *
from calculo import calculo
class Principal():

    def __init__(self):
        self.dato=None


    def mostrar(self):
        ventana=Tk()
        ventana.title("Principal")
        ventana.geometry('700x600')
        ventana.resizable(width=False,height=False)
        #----------- imagen de fondo
        icono=PhotoImage(file="../imagenes/Opc.png")
        Limg=Label(ventana,image=icono).pack()

        
        def cimiento():
            ventana.destroy()
            x=calculo()
            x.cimiento()
            #self.dato="cimiento"

        def pared():
            ventana.destroy()
            x=calculo()
            x.pared()
            #self.dato="pared"

        def contrapiso():
            ventana.destroy()
            x=calculo()
            x.contrapiso()
            #self.dato="contrapiso"

        def revoque():
            ventana.destroy()
            x=calculo()
            x.revoque()
            #self.dato="revoque"

        def techo():
            ventana.destroy()
            x=calculo()
            x.techo()
            #self.dato="revoque"

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
        ventana.mainloop()
        return self.dato
#-----------------------
#a=Principal()
#a.mostrar()
#print(a.dato)