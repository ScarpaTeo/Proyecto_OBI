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
        self.resultado=""

    #a esta funcion le pasas el string de resultado y la variable resultado le agregas al textFile
    def cargarResultado(self,resu):
        self.resultado=resu
        
    def vistaTecho(self):

        def calcular():
            alto=float(Calto.get())
            ancho=float(Cancho.get())
            tipo=str(Ccombo.get())
            self.valor={
                "alto":alto,
                "ancho":ancho,
                "tipo":tipo
            }
        def volverAtras():
            ventana.destroy()
            self.valor=True

        ventana=Tk()
        ventana.title('Calcular de Techo')
        ventana.geometry('700x600')
        img=PhotoImage(file="../imagenes/techo.png")
        Licono=Label(ventana,image=img).pack()

        #--------------combo box tipo de pared
        Ccombo = ttk.Combobox(values=["1.83","2.13","2.44","2.74","3.05","3.36","3.66","3.96"],state="readonly",font=('Arial',12))
        Ccombo.configure(width=6)
        Ccombo.place(x=129,y=168)
        #--------------------campo Alto
        Calto=Entry(ventana,width=14,relief="flat",bg="#FEE780",font=('Arial',16))
        Calto.place(x=128,y=249)

        #-------------------campo ancho
        Cancho=Entry(ventana,width=14,relief="flat",bg="#FEE780",font=('Arial',16))
        Cancho.place(x=128,y=331)

        #------------------------Text field
        Dtextfiel=Text(ventana,width=21,height=13,relief="flat",bg="#FFFFFF",font=('Arial',14))
        Dtextfiel.place(x=316 ,y=150)
        Dtextfiel.insert(INSERT,self.resultado)
        Dtextfiel.configure(state='disabled')


        #---------boton calcular
        BcalcularCimiento=Button(ventana,width=11,relief="flat",bg="#FFDE00",font=('Arial',18),text="Calcular",command=calcular).place(x=131,y=454)

        #--------boton atras
        Batras=Button(ventana,width=4,relief="flat",bg="#FFFFFF",font=('Arial',16),text="Atras",command=volverAtras).place(x=518,y=89)
        ventana.mainloop()
        return self.valor

