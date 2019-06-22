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

class Cimiento():
    def __init__(self):
        self.valor=False
        #variable para cargar el resultado
        self.resultado=""
    
    #a esta funcion le pasas el string de resultado y la variable resultado le agregas al textFile
    def cargarResultado(self,resu):
        self.resultado=resu

    def vistaCimiento(self):

        def calcular():
            alto=float(Calto.get())
            ancho=float(Cancho.get())
            profundidad=float(Cprofundidad.get())
            tipo_a_calcular=str(Ctipo.get())

            self.valor={
                "alto":alto,
                "ancho":ancho,
                "profundidad":profundidad,
                "tipo_a_calcular":tipo_a_calcular
            }

        def volverAtras():
            ventana.destroy()
            self.valor=True

        ventana=Tk()
        ventana.title('Calcular Cimiento')
        ventana.geometry('700x600')
        img=PhotoImage(file="../imagenes/cimiento.png")
        Licono=Label(ventana,image=img).pack()

        #--------------combo box
        Ccombo = ttk.Combobox(values=["Corrida", "viga", "pilotin"],state="readonly",width=16,font=('Arial',12))
        Ccombo.place(x=128,y=140)

        #--------------------campo y label Alto
        Calto=Entry(ventana,width=14,relief="flat",bg="#FEE780",font=('Arial',16))
        Calto.place(x=128,y=220)

        #-------------------campo y laber ancho
        Cancho=Entry(ventana,width=14,relief="flat",bg="#FEE780",font=('Arial',16))
        Cancho.place(x=128,y=303)

        #---------------campo y label profundidad
        Cprofundidad=Entry(ventana,width=14,relief="flat",bg="#FEE780",font=('Arial',16))
        Cprofundidad.place(x=128,y=388)

        #------------------------Text field
        Dtextfiel=Text(ventana,width=21,height=13,relief="flat",bg="#FFFFFF",font=('Arial',18)).place(x=316 ,y=150)

        #---------boton calcular
        BcalcularCimiento=Button(ventana,width=11,relief="flat",bg="#FFDE00",font=('Arial',18),text="Calcular",command=calcular).place(x=131,y=454)

        # ---------boton atras
        Batras=Button(ventana,width=4,relief="flat",bg="#FFFFFF",font=('Arial',16),text="Atras",command=volverAtras).place(x=518,y=89)

        ventana.mainloop()
        return self.valor
        #ventana para el calculo de contrapiso