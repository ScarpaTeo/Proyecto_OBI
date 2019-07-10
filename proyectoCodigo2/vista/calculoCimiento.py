# esto sirve para insertar por lineas en los textfield en el Tkinter
#T.insert(tk.END, "Just a text Widget\nin two lines\n")

#como enviar texto a los textfield
#text.configure(state='normal')
#text.insert('end', 'Some Text')
#text.configure(state='disabled')

from tkinter import *
import tkinter.ttk as ttk
from animaciones import *

class Cimiento():

    def __init__(self):
        self.valor=False
        #variable para cargar el resultado
    def vistaCimiento(self,resultado="",estado="normal"):
        def errorVacio():
            error.config(text="error! campos vacios")
        def errorIncorrecto():
            error.config(text="error! valores incorrectos")
            
        def pressEnter(evento):
            calcular()
        
        ventana=Tk()
        ventana.title('Calcular Cimiento')
        ventana.geometry('700x600+350+0')
        ventana.bind("<Return>",pressEnter)
        img=PhotoImage(file="../imagenes/cimiento.png")
        Licono=Label(ventana,image=img).pack()
        error=Label(ventana,text="",bg="white",fg="red",font=("Arial",12))
        error.place(x=253, y=80)
        
        def calcular():
            if not Calto.get() or not Cancho.get() or not Cprofundidad.get() or not Ccombo.get():
                errorVacio()
                Calto.delete(0,END)
                Cancho.delete(0,END)
                Cprofundidad.delete(0,END)
            else:
                try:
                    alto=float(Calto.get())
                    ancho=float(Cancho.get())
                    profundidad=float(Cprofundidad.get())
                    tipo_a_calcular=str(Ccombo.get())
                except Exception:
                    errorIncorrecto()
                    Calto.delete(0,END)
                    Cancho.delete(0,END)
                    Cprofundidad.delete(0,END)
                self.valor={
                    "alto":alto,
                    "ancho":ancho,
                    "profundidad":profundidad,
                    "tipo_a_calcular":tipo_a_calcular
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

        #--------------combo box
        Ccombo = ttk.Combobox(values=["Zapata Corrida", "Viga de Hormigón", "Pilotin de Hormigón"],state="readonly",width=16,font=('Arial',12))
        Ccombo.place(x=101,y=138)

        #--------------------campo y label Alto#FEE780
        Calto=Entry(ventana,width=15,relief="flat",bg="#FEE780",font=('Arial',15))
        Calto.place(x=101,y=218)

        #-------------------campo y laber ancho
        Cancho=Entry(ventana,width=15,relief="flat",bg="#FEE780",font=('Arial',15))
        Cancho.place(x=101,y=301)

        #---------------campo y label profundidad
        Cprofundidad=Entry(ventana,width=14,relief="flat",bg="#FEE780",font=('Arial',16))
        Cprofundidad.place(x=101,y=385)

        #------------------------Text field
        Dtextfiel=Text(ventana,width=23,height=12,relief="flat",bg="#FFFFFF",font=('Arial',14))
        Dtextfiel.place(x=350 ,y=143)
        Dtextfiel.insert(INSERT,resultado)
        Dtextfiel.configure(state='disabled')

        #---------boton calcular
        if estado =="normal":
            BcalcularCimiento=Button(ventana,width=12,relief="flat",activebackground="#FFDE00",bg="#FFDE00",font=('Arial',18),text="Calcular",command=calcular).place(x=97,y=450)
            #--------------seguir calculando
            Bañadir=Button(ventana,state=DISABLED,width=8,relief="flat",activebackground="#FFDE00",bg="#FFDE00",font=('Arial',10),text="añadir",command=añadir).place(x=371,y=460)
             #-------------imprimir detalle
            Bimprimir=Button(ventana,state=DISABLED,width=8,relief="flat",activebackground="#FFDE00",bg="#FFDE00",font=('Arial',10),text="imprimir",command=volverAtras).place(x=517,y=460)
        else:
            #--------------seguir calculando
            Bañadir=Button(ventana,width=8,relief="flat",activebackground="#FFDE00",bg="#FFDE00",font=('Arial',10),text="añadir",command=añadir).place(x=371,y=460)
            BcalcularCimiento=Button(ventana,state=DISABLED,width=12,relief="flat",activebackground="#FFDE00",bg="#FFDE00",font=('Arial',18),text="Calcular",command=calcular).place(x=97,y=450)

             #-------------imprimir detalle
            Bimprimir=Button(ventana,width=8,relief="flat",activebackground="#FFDE00",bg="#FFDE00",font=('Arial',10),text="imprimir",command=volverAtras).place(x=517,y=460)
        # ---------boton atras
        Batras=Button(ventana,width=8,relief="flat",activebackground="#FFFFFF",bg="#FFFFFF",font=('Arial',10),text="Atras",command=volverAtras).place(x=545,y=75)
        bt_ayuda = Button(ventana, text="Ayuda",command=animacion, fg="#FFDE00",activebackground="#1E1E1E", bg="#1E1E1E", relief="flat", height=1, width=4).place(x=10, y=563)

        
      
        ventana.focus_force()
        ventana.mainloop()
        return self.valor

#x=Cimiento()
#x.vistaCimiento()
#print(x.valor)