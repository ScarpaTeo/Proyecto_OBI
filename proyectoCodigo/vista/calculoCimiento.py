# esto sirve para insertar por lineas en los textfield en el Tkinter
#T.insert(tk.END, "Just a text Widget\nin two lines\n")

#como enviar texto a los textfield
#text.configure(state='normal')
#text.insert('end', 'Some Text')
#text.configure(state='disabled')

from tkinter import *
import tkinter.ttk as ttk

class Cimiento():

    def __init__(self):
        self.valor=False
        #variable para cargar el resultado
    def vistaCimiento(self,resultado="",estado="normal"):
        ventana=Tk()
        ventana.title('Calcular Cimiento')
        ventana.geometry('700x600')
        img=PhotoImage(file="../imagenes/cimiento.png")
        Licono=Label(ventana,image=img).pack()

        def errorVacio():
            error=Label(ventana,text="*error campos vacios*",bg="white",fg="red",font=("Arial",12)).place(x=253, y=80)
        def errorIncorrecto():
            error=Label(ventana,text="*error valores incorrectos*",bg="white",fg="red",font=("Arial",12)).place(x=253, y=80)
        
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
        Dtextfiel=Text(ventana,width=21,height=13,relief="flat",bg="#FFFFFF",font=('Arial',14))
        Dtextfiel.place(x=316 ,y=150)
        Dtextfiel.insert(INSERT,resultado)
        Dtextfiel.configure(state='disabled')

        #---------boton calcular
        if estado =="normal":
            BcalcularCimiento=Button(ventana,width=11,relief="flat",bg="#FFDE00",font=('Arial',18),text="Calcular",command=calcular).place(x=131,y=454)
        else:
            BcalcularCimiento=Button(ventana,state=DISABLED,width=11,relief="flat",bg="#FFDE00",font=('Arial',18),text="Calcular",command=calcular).place(x=131,y=454)
        # ---------boton atras
        Batras=Button(ventana,width=4,relief="flat",bg="#FFFFFF",font=('Arial',16),text="Atras",command=volverAtras).place(x=518,y=89)

        ventana.mainloop()
        return self.valor
