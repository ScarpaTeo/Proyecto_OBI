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

class Contrapiso():
    def __init__(self):
        self.valor=False
        self.resultado=""
    
    
    def vistaContrapiso(self):

        def calcular():
            alto=float(Calto.get())
            ancho=float(Cancho.get())
            profundidad=float(Cprofundidad.get())
            tipo=str(Ctipo.get())
            self.valor={
                "alto":alto,
                "ancho":ancho,
                "profundidad":profundidad
                "tipo":tipo
            }

        def volverAtras():
            ventana.destroy()
            self.valor=True

        ventana=Tk()
        ventana.title('Calcular Contrapiso')
        ventana.geometry('700x600')
        img=PhotoImage(file="../imagenes/contrapiso.png")
        Licono=Label(ventana,image=img).pack()

        #--------------------campo Alto
        Calto=Entry(ventana,width=14,relief="flat",bg="#FEE780",font=('Arial',16))
        Calto.place(x=128,y=175)

        #-------------------campo ancho
        Cancho=Entry(ventana,width=14,relief="flat",bg="#FEE780",font=('Arial',16))
        Cancho.place(x=128,y=259)

        #---------------campo profundidad
        Cprofundidad=Entry(ventana,width=14,relief="flat",bg="#FEE780",font=('Arial',16))
        Cprofundidad.place(x=128,y=342)

        #------------------------Text field
        Dtextfiel=Text(ventana,width=21,height=13,relief="flat",bg="#FFFFFF",font=('Arial',18)).place(x=316 ,y=150)

        #---------boton calcular
        BcalcularCimiento=Button(ventana,width=11,relief="flat",bg="#FFDE00",font=('Arial',18),text="Calcular",command=calcular).place(x=131,y=454)

        # ---------boton atras
        Batras=Button(ventana,width=4,relief="flat",bg="#FFFFFF",font=('Arial',16),text="Atras").place(x=518,y=89)
        ventana.mainloop()
        return self.valor
