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


class Pared():
    def __init__(self):
        self.valor=False

    def vistaPared(self, resultado="",estado="normal"):
        def errorVacio():
            error.config(text="error! campos vacios")
        def errorIncorrecto():
            error.config(text="error! valores incorrectos")

        def pressEnter(evento):
            calcular()
           
        ventana=Tk()
        ventana.title('Calcular Pared')
        ventana.geometry('700x600+350+0')
        ventana.bind("<Return>", pressEnter)
        img=PhotoImage(file="../imagenes/pared.png")
        Licono=Label(ventana,image=img).pack()
        error=Label(ventana,text="",bg="white",fg="red",font=("Arial",12))
        error.place(x=253, y=80)
        
        def calcular():
            if not Calto.get() or not Cancho.get() or not Ccombo.get() or not Cespesor.get():
                errorVacio()
                Calto.delete(0,END)
                Cancho.delete(0,END)
                Ccombo.delete(0,END)
                Cespesor.delete(0,END)
            else:
                try:
                    alto=float(Calto.get())
                    ancho=float(Cancho.get())
                    tipo=str(Ccombo.get())
                    espesor=str(Cespesor.get())
                except Exception:
                    errorIncorrecto()
                    Calto.delete(0,END)
                    Cancho.delete(0,END)
                    Ccombo.delete(0,END)
                    Cespesor.delete(0,END)
                self.valor={
                    "alto":alto,
                    "ancho":ancho,
                    "tipo":tipo,
                    "espesor":espesor
                }
                ventana.destroy()

        def volverAtras():
            ventana.destroy()
            self.valor="principal"

        #--------------combo box tipo de pared
        Ccombo = ttk.Combobox(values=["Pared de Bloques", "Pared de Tabiques", "Pared Común"],state="readonly",font=('Arial',12))
        Ccombo.configure(width=16)
        Ccombo.place(x=105,y=136)
        #--------------------campo Alto
        Calto=Entry(ventana,width=14,relief="flat",bg="#FEE780",font=('Arial',16))
        Calto.place(x=101,y=216)

        #-------------------campo ancho
        Cancho=Entry(ventana,width=14,relief="flat",bg="#FEE780",font=('Arial',16))
        Cancho.place(x=101,y=297)

        #---------------combox espesor
        Cespesor= ttk.Combobox(values=["0.15 cm", "0.20 cm", "0.30 cm"],state="readonly",font=('Arial',11))
        Cespesor.configure(width=9)
        Cespesor.place(x=106,y=385)

        #------------------------Text field
        Dtextfiel=Text(ventana,width=24,height=12,relief="flat",bg="#FFFFFF",font=('Arial',14))
        Dtextfiel.place(x=344 ,y=138)
        Dtextfiel.insert(INSERT,resultado)
        Dtextfiel.configure(state='disabled')
        if estado=="normal":
        #---------boton calcular
            BcalcularCimiento=Button(ventana,width=12,relief="flat",bg="#FFDE00",font=('Arial',18),text="Calcular",command=calcular).place(x=99,y=448)
        else:
            BcalcularCimiento=Button(ventana,state=DISABLED,width=12,relief="flat",bg="#FFDE00",font=('Arial',18),text="Calcular",command=calcular).place(x=99,y=448)

        #--------boton atras
        Batras=Button(ventana,width=8,relief="flat",bg="#FFFFFF",font=('Arial',10),text="Atras",command=volverAtras).place(x=543,y=70)
        #-------------imprimir detalle
        Bimprimir=Button(ventana,width=8,relief="flat",bg="#FFDE00",font=('Arial',10),text="imprimir",command=volverAtras).place(x=516,y=458)
        #--------------seguir calculando
        Bañadir=Button(ventana,width=8,relief="flat",bg="#FFDE00",font=('Arial',10),text="añadir",command=volverAtras).place(x=369,y=458)
        ventana.focus_force()        
        ventana.mainloop()
        return self.valor

#x=Pared()
#x.vistaPared()
#print(x.valor)