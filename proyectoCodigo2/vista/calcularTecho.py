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

class Techo():
    def __init__(self):
        self.valor=False

    
    def vistaTecho(self,resultado="",estado="normal"):
        def errorVacio():
            error.config(text="error! campos vacios")
        def errorIncorrecto():
            error.config(text="error! valores incorrectos")
        
        def pressEnter(evento):
            calcular()

        ventana=Tk()
        ventana.title('Calcular de Techo')
        ventana.geometry('700x600+350+0')
        ventana.bind("<Return>",pressEnter)
        img=PhotoImage(file="../imagenes/techo.png")
        Licono=Label(ventana,image=img).pack()
        error=Label(ventana,text="",bg="white",fg="red",font=("Arial",12))
        error.place(x=253, y=80)
        
        def calcular():
            if not Calto.get() or not Calto.get() or not Ccombo.get():
                errorVacio()
                Calto.delete(0,END)
                Cancho.delete(0,END)
            else:
                try:
                    alto=float(Calto.get())
                    ancho=float(Calto.get())
                    tipo=float(Ccombo.get())
                except Exception:
                    errorIncorrecto()
                    Calto.delete(0,END)
                    Cancho.delete(0,END)
                self.valor={
                    "alto":alto,
                    "ancho":ancho,
                    "tipo":tipo
                }
                ventana.destroy()

        def volverAtras():
            ventana.destroy()
            self.valor="principal"

        #--------------combo box tipo de pared
        Ccombo = ttk.Combobox(values=["1.83","2.13","2.44","2.74","3.05","3.36","3.66","3.96"],state="readonly",font=('Arial',12))
        Ccombo.configure(width=16)
        Ccombo.place(x=105,y=200)
        #--------------------campo Alto
        Calto=Entry(ventana,width=14,relief="flat",bg="#FEE780",font=('Arial',16))
        Calto.place(x=105,y=281)

        #-------------------campo ancho
        Cancho=Entry(ventana,width=14,relief="flat",bg="#FEE780",font=('Arial',16))
        Cancho.place(x=105,y=365)

        #------------------------Text field
        Dtextfiel=Text(ventana,width=24,height=12,relief="flat",bg="#FFFFFF",font=('Arial',14))
        Dtextfiel.place(x=345 ,y=155)
        Dtextfiel.insert(INSERT,resultado)
        Dtextfiel.configure(state='disabled')

        if estado=="normal":
        #---------boton calcular
            BcalcularCimiento=Button(ventana,width=11,relief="flat",bg="#FFDE00",font=('Arial',19),text="Calcular",command=calcular).place(x=101,y=464)
        else:
            BcalcularCimiento=Button(ventana,state=DISABLED,width=11,relief="flat",bg="#FFDE00",font=('Arial',19),text="Calcular",command=calcular).place(x=101,y=464)
        #--------boton atras
        Batras=Button(ventana,width=8,relief="flat",bg="#FFFFFF",font=('Arial',10),text="Atras",command=volverAtras).place(x=543,y=91)
        #-------------imprimir detalle
        Bimprimir=Button(ventana,width=8,relief="flat",bg="#FFDE00",font=('Arial',10),text="imprimir",command=volverAtras).place(x=516,y=475)
        #--------------seguir calculando
        Bañadir=Button(ventana,width=8,relief="flat",bg="#FFDE00",font=('Arial',10),text="añadir",command=volverAtras).place(x=369,y=475)
        
        ventana.focus_force()        
        ventana.mainloop()
        return self.valor

#x=Techo()
#x.vistaTecho()