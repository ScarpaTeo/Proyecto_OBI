from tkinter import *
from calculo import calculo
class Principal():

    def __init__(self):
        self.dato=None


    def mostrar(self):
        ventana=Tk()
        ventana.title("Principal")
        ventana.geometry('500x310')
        ventana.resizable(width=False,height=False)

        
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
            self.dato="revoque"

        Bcimiento=Button(ventana, text="Cimiento",fg="white",bg="#848484", font=("Arial",24),width=23, height=1, command=cimiento)
        Bcimiento.place(x=30, y=10)

        Bpared=Button(ventana, text="Pared",fg="white",bg="#848484", font=("Arial",24),width=23, height=1,command=pared)
        Bpared.place(x=30,y=70)

        Bcontrapiso=Button(ventana, text="Contrapiso",fg="white",bg="#848484", font=("Arial",24),width=23, height=1,command=contrapiso)
        Bcontrapiso.place(x=30, y=130)

        Brevoque=Button(ventana, text="Revoque",fg="white",bg="#848484", font=("Arial",24),width=23, height=1,command=revoque)
        Brevoque.place(x=30, y=190)

        Btecho=Button(ventana, text="Techo",fg="white",bg="#848484", font=("Arial",24),width=23, height=1,command=techo)
        Btecho.place(x=30, y=250)
        ventana.mainloop()
        return self.dato