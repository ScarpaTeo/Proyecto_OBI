# esto sirve para insertar por lineas en los textfield en el Tkinter
#T.insert(tk.END, "Just a text Widget\nin two lines\n")

#como enviar texto a los textfield
#text.configure(state='normal')
#text.insert('end', 'Some Text')
#text.configure(state='disabled')

from tkinter import *
import tkinter.ttk as ttk
# import sys
# sys.path.append('../calculos')
# from calculo import *


class Revoque():
    def __init__(self):
        self.valor=False
    def vistaRevoque(self,resultado=""):
        def calcular():
            alto=float(Calto.get())
            ancho=float(Cancho.get())
            tipo=str(Ccombo.get())
            self.valor={
                "alto":alto,
                "ancho":ancho,
                "tipo":tipo
            }
            ventana.destroy()
        def volverAtras():
            ventana.destroy()
            self.valor=True

        ventana=Tk()
        ventana.title('Calcular Reboques')
        ventana.geometry('700x600')
        img=PhotoImage(file="../imagenes/revoque.png")
        Licono=Label(ventana,image=img).pack()

        #--------------combo box tipo de pared
        Ccombo = ttk.Combobox(values=["Revoque Impearmeable", "Reboque Grueso", "Reboque fino"],state="readonly",font=('Arial',12))
        Ccombo.configure(width=16)
        Ccombo.place(x=128,y=168)
        #--------------------campo Alto
        Calto=Entry(ventana,width=14,relief="flat",bg="#FEE780",font=('Arial',16))
        Calto.place(x=128,y=249)

        #-------------------campo ancho
        Cancho=Entry(ventana,width=14,relief="flat",bg="#FEE780",font=('Arial',16))
        Cancho.place(x=128,y=332)

        #------------------------Text field
        Dtextfiel=Text(ventana,width=21,height=13,relief="flat",bg="#FFFFFF",font=('Arial',14))
        Dtextfiel.place(x=316 ,y=150)
        Dtextfiel.insert(INSERT,resultado)
        Dtextfiel.configure(state='disabled')

        #---------boton calcular
        BcalcularCimiento=Button(ventana,width=11,relief="flat",bg="#FFDE00",font=('Arial',18),text="Calcular",command=calcular).place(x=131,y=454)

        #--------boton atras
        Batras=Button(ventana,width=4,relief="flat",bg="#FFFFFF",font=('Arial',16),text="Atras",command=volverAtras).place(x=518,y=89)
        ventana.mainloop()
        return self.valor