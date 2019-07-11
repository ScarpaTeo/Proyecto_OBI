# esto sirve para insertar por lineas en los textfield en el Tkinter
#T.insert(tk.END, "Just a text Widget\nin two lines\n")

#como enviar texto a los textfield
#text.configure(state='normal')
#text.insert('end', 'Some Text')
#text.configure(state='disabled')

from tkinter import *
import tkinter.ttk as ttk
from animaciones import *
# import sys
# sys.path.append('../calculos')
# from calculo import *


class Revoque():
    def __init__(self):
        self.valor=False
    def vistaRevoque(self,resultado="",estado="normal"):
        def errorVacio():
            error.config(text="error! campos vacios")
        def errorIncorrecto():
            error.config(text="error! valores incorrectos")
        
        def pressEnter(evento):
            calcular()
           
        ventana=Tk()
        ventana.title('Calcular Revoques')
        ventana.geometry('700x600+350+0')
        ventana.bind("<Return>", pressEnter)
        img=PhotoImage(file="../imagenes/revoque.png")
        Licono=Label(ventana,image=img).pack()
        error=Label(ventana,text="",bg="white",fg="red",font=("Arial",12))
        error.place(x=253, y=80)

        def calcular():
            if not Calto.get() or not Cancho.get() or not Ccombo.get():
                errorVacio()
                Calto.delete(0,END)
                Cancho.delete(0,END)
                Ccombo.delete(0,END)
            else:
                try:
                    alto=float(Calto.get())
                    ancho=float(Cancho.get())
                    tipo=str(Ccombo.get())
                except Exception:
                    errorIncorrecto()
                    Calto.delete(0,END)
                    Cancho.delete(0,END)
                    Ccombo.delete(0,END)
                self.valor={
                    "alto":alto,
                    "ancho":ancho,
                    "tipo":tipo
                }
                ventana.destroy()
        def volverAtras():
            ventana.destroy()
            self.valor="principal"
        def añadir():
            ventana.destroy()
            self.valor="añadir"
        def imprimir():
            ventana.destroy()
            self.valor="imprimir"

        def animacion():
            x=Mensajes()
            x.mensajecalculos()
        #--------------combo box tipo de pared
        Ccombo = ttk.Combobox(values=["Revoque Exterior Completo", "Revoque Interior Completo"],state="readonly",font=('Arial',12))
        Ccombo.configure(width=16)
        Ccombo.place(x=107,y=197)
        #--------------------campo Alto#FEE780
        Calto=Entry(ventana,width=15,relief="flat",bg="#FEE780",font=('Arial',15))
        Calto.place(x=106,y=278)

        #-------------------campo ancho
        Cancho=Entry(ventana,width=15,relief="flat",bg="#FEE780",font=('Arial',15))
        Cancho.place(x=106,y=362)

        #------------------------Text field
        Dtextfiel=Text(ventana,width=24,height=12,relief="flat",bg="#FFFFFF",font=('Arial',14))
        Dtextfiel.place(x=344 ,y=154)
        Dtextfiel.insert(INSERT,resultado)
        Dtextfiel.configure(state='disabled')

        if estado=="normal":
        #---------boton calcular
            BcalcularCimiento=Button(ventana,width=12,relief="flat",activebackground="#FFDE00",bg="#FFDE00",font=('Arial',18),text="Calcular",command=calcular).place(x=103,y=462)
            #--------------seguir calculando
            Bañadir=Button(ventana,state=DISABLED,width=8,relief="flat",activebackground="#FFDE00",bg="#FFDE00",font=('Arial',10),text="añadir",command=añadir).place(x=371,y=471)
            #-------------imprimir detalle
            Bimprimir=Button(ventana,state=DISABLED,width=8,relief="flat",activebackground="#FFDE00",bg="#FFDE00",font=('Arial',10),text="imprimir",command=imprimir).place(x=518,y=471)
        else:
            BcalcularCimiento=Button(ventana,state=DISABLED,width=12,relief="flat",activebackground="#FFDE00",bg="#FFDE00",font=('Arial',18),text="Calcular",command=calcular).place(x=103,y=462)
            #--------------seguir calculando
            Bañadir=Button(ventana,width=8,relief="flat",activebackground="#FFDE00",bg="#FFDE00",font=('Arial',10),text="añadir",command=añadir).place(x=371,y=471)
            #-------------imprimir detalle
            Bimprimir=Button(ventana,width=8,relief="flat",activebackground="#FFDE00",bg="#FFDE00",font=('Arial',10),text="imprimir",command=imprimir).place(x=518,y=471)
        #--------boton atras
        Batras=Button(ventana,width=8,relief="flat",activebackground="#FFFFFF",bg="#FFFFFF",font=('Arial',10),text="Atras",command=volverAtras).place(x=546,y=87)
        bt_ayuda = Button(ventana, text="Ayuda",command=animacion, fg="#FFDE00",activebackground="#1E1E1E", bg="#1E1E1E", relief="flat", height=1, width=4).place(x=10, y=563)

        
       
        ventana.focus_force()        
        ventana.mainloop()
        return self.valor

#x=Revoque()
#x.vistaRevoque()