from tkinter import *
class Principal():
    def __init__(self):
        ventana=Tk()
        ventana.title("Principal")
        ventana.geometry('500x310')
        ventana.resizable(width=False,height=False)

        Bcimiento=Button(ventana, text="Cimiento",fg="white",bg="#848484", font=("Arial",24),width=23, height=1)
        Bcimiento.place(x=30, y=10)

        Bpared=Button(ventana, text="Pared",fg="white",bg="#848484", font=("Arial",24),width=23, height=1)
        Bpared.place(x=30,y=70)

        Bcontrapiso=Button(ventana, text="Contrapiso",fg="white",bg="#848484", font=("Arial",24),width=23, height=1)
        Bcontrapiso.place(x=30, y=130)

        Brevoque=Button(ventana, text="Revoque",fg="white",bg="#848484", font=("Arial",24),width=23, height=1)
        Brevoque.place(x=30, y=190)

        Btecho=Button(ventana, text="Contrapiso",fg="white",bg="#848484", font=("Arial",24),width=23, height=1)
        Btecho.place(x=30, y=250)
        ventana.mainloop()