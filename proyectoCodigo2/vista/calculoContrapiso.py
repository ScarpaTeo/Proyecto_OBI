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

class Contrapiso():
    def __init__(self):
        self.valor=False
    
    def vistaContrapiso(self,resultado="",estado="normal"):
        def errorVacio():
            error.config(text="error! campos vacios")
        def errorIncorrecto():
            error.config(text="error! valores incorrectos")
        
        def pressEnter(evento):
            calcular()
           
        ventana=Tk()
        ventana.title('Calcular Contrapiso')
        ventana.geometry('700x600+350+0')
        ventana.bind("<Return>",pressEnter)
        img=PhotoImage(file="../imagenes/contrapiso.png")
        Licono=Label(ventana,image=img).pack()
        error=Label(ventana,text="",bg="white",fg="red",font=("Arial",12))
        error.place(x=253, y=80)
        
        
        def calcular():
            if not Calto.get() or not Cancho.get() or not Cprofundidad.get():
                errorVacio()
                Calto.delete(0,END)
                Cancho.delete(0,END)
                Cprofundidad.delete(0,END)
            else:
                try:
                    alto=float(Calto.get())
                    ancho=float(Cancho.get())
                    profundidad=float(Cprofundidad.get())
                except Exception:
                    errorIncorrecto()
                    Calto.delete(0,END)
                    Cancho.delete(0,END)
                    Cprofundidad.delete(0,END)
                self.valor={
                    "alto":alto,
                    "ancho":ancho,
                    "profundidad":profundidad
                }
                ventana.destroy()

        def volverAtras():
            ventana.destroy()
            self.valor="principal"
        def añadir():
            ventana.destroy()
            self.valor="añadir"
        def animacion():
            x=Mensajes()
            x.mensajecalculos()
        #--------------------campo Alto#FEE780
        Calto=Entry(ventana,width=15,relief="flat",bg="#FEE780",font=('Arial',15))
        Calto.place(x=106,y=196)

        #-------------------campo ancho
        Cancho=Entry(ventana,width=15,relief="flat",bg="#FEE780",font=('Arial',15))
        Cancho.place(x=106,y=279)

        #---------------campo profundidad
        Cprofundidad=Entry(ventana,width=15,relief="flat",bg="#FEE780",font=('Arial',15))
        Cprofundidad.place(x=106,y=363)

        #------------------------Text field
        Dtextfiel=Text(ventana,width=24,height=12,relief="flat",bg="#FFFFFF",font=('Arial',14))
        Dtextfiel.place(x=345 ,y=155)
        Dtextfiel.insert(INSERT,resultado)
        Dtextfiel.configure(state='disabled')

        if estado=="normal":
            #---------boton calcular
            BcalcularCimiento=Button(ventana,width=12,relief="flat",bg="#FFDE00",font=('Arial',18),text="Calcular",command=calcular).place(x=101,y=462)
            #--------------seguir calculando
            Bañadir=Button(ventana,state=DISABLED,width=8,relief="flat",bg="#FFDE00",font=('Arial',10),text="añadir",command=añadir).place(x=371,y=472)
            #-------------imprimir detalle
            Bimprimir=Button(ventana,state=DISABLED,width=8,relief="flat",bg="#FFDE00",font=('Arial',10),text="imprimir",command=volverAtras).place(x=517,y=472)
        else:
            BcalcularCimiento=Button(ventana,state=DISABLED,width=12,relief="flat",bg="#FFDE00",font=('Arial',18),text="Calcular",command=calcular).place(x=101,y=462)
            #--------------seguir calculando
            Bañadir=Button(ventana,width=8,relief="flat",bg="#FFDE00",font=('Arial',10),text="añadir",command=añadir).place(x=371,y=472)
            #-------------imprimir detalle
            Bimprimir=Button(ventana,width=8,relief="flat",bg="#FFDE00",font=('Arial',10),text="imprimir",command=volverAtras).place(x=517,y=472)
        # ---------boton atras
        Batras=Button(ventana,width=8,relief="flat",bg="#FFFFFF",font=('Arial',10),text="Atras",command=volverAtras).place(x=546,y=88)
        bt_ayuda = Button(ventana, text="Ayuda",command=animacion, fg="#FFDE00", bg="#1E1E1E", relief="flat", height=1, width=4).place(x=10, y=563)

        ventana.focus_force()        
        ventana.mainloop()
        return self.valor

#x=Contrapiso()
#x.vistaContrapiso()