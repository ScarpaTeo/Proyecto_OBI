from tkinter import *
class Principal():
    def cargar(self):

        ventana=Tk()
        ventana.title("Principal")
        ventana.geometry('400x310')

        LFondo= PhotoImage("")
        
        Bcimiento=Button(ventana, text="Cimiento", width=42, height=2)
        Bcimiento.place(x=20, y=10)

        Bpared=Button(ventana, text="Pared", width=42, height=2)
        Bpared.place(x=20, y=70)

        Bcontrapiso=Button(ventana, text="Contrapiso", width=42, height=2)
        Bcontrapiso.place(x=20, y=130)

        Brevoque=Button(ventana, text="Revoque", width=42, height=2)
        Brevoque.place(x=20, y=190)

        Btecho=Button(ventana, text="Contrapiso", width=42, height=2)
        Btecho.place(x=20, y=250)
        ventana.mainloop()
