# esto sirve para insertar por lineas en los textfield en el Tkinter
#T.insert(tk.END, "Just a text Widget\nin two lines\n")

#como enviar texto a los textfield
#text.configure(state='normal')
#text.insert('end', 'Some Text')
#text.configure(state='disabled')

from tkinter import *
import tkinter.ttk as ttk
from animaciones import *

class ActualizarPrecio():
    def __init__(self):
        self.valor=False

    
    def vistaActualizar(self,resultado="",estado="normal",datos=""):
        def errorVacio():
            error.config(text="error! campos vacios")
        def errorIncorrecto():
            error.config(text="error! valores incorrectos")

        def pressEnter(evento):
            actulizar()

        ventana=Tk()
        ventana.title('Actualizar Precios')
        ventana.geometry('700x600+350+0')
        ventana.bind("<Return>",pressEnter)
        img=PhotoImage(file="../imagenes/Precios.png")
        Licono=Label(ventana,image=img).pack()
        error=Label(ventana,text=resultado,bg="white",fg="red",font=("Arial",12))
        error.place(x=253, y=80)


        def actulizar():
            if  not Cprecio.get() or not Ccombo.get():
                errorVacio()
                Cprecio.delete(0,END)
                Ccombo.delete(0,END)
            else:
                try:
                    tipo=str(Ccombo.get())
                    precio=float(Cprecio.get())
                    if tipo=="Cal":
                        precio=precio/20
                    elif tipo=="Cemento":
                        precio=precio/50
                    elif tipo=="Hierro del 10":
                        precio=precio/12
                    elif tipo=="Hierro del 4":
                        precio=precio/12


                except Exception:
                    errorIncorrecto()
                    Ccombo.delete(0,END)
                    Cprecio.delete(0,END)
                self.valor={
                    "tipo":tipo,
                    "precio":precio
                }
                ventana.destroy()

        def volverAtras():
            ventana.destroy()
            self.valor="principal"
        def animacion():
            x=Mensajes()
            x.mensajePrecios()
   

         #--------------combo box tipo de pared
        Ccombo = ttk.Combobox(values=["Arena","Cal","Cemento","Hierro del 10","Hierro del 4","Piedra","Ladrillo Común 0,15","Bloque Ceramico 0,15","Bloque Ceramico 0,20","Bloque Hormigón 0,15","Bloque Hormigón 0,20"],state="readonly",font=('Arial',12))
        Ccombo.configure(width=16)
        Ccombo.place(x=129,y=219)

        #-------------------campo Precio
        Cprecio=Entry(ventana,width=15,relief="flat",bg="#FEE780",font=('Arial',15))
        Cprecio.place(x=128,y=321)

        #------------------------Text field
        Dtextfiel=Text(ventana,width=26,height=13,relief="flat",bg="#FFFFFF",font=('Arial',12))
        Dtextfiel.place(x=342 ,y=180)
        Dtextfiel.insert(INSERT,datos)
        Dtextfiel.configure(state='disabled')
    
        if estado=="normal":
        #---------boton Actualizar#FFDE00
            BcalcularCimiento=Button(ventana,width=11,relief="flat",bg="#FFDE00",font=('Arial',18),text="Actualizar",command=actulizar).place(x=136,y=447)
        #--------boton atras
        Batras=Button(ventana,width=8,relief="flat",bg="#FFFFFF",font=('Arial',10),text="Atras",command=volverAtras).place(x=514,y=85)
        bt_ayuda = Button(ventana, text="Ayuda", fg="#FFDE00", bg="#1E1E1E", relief="flat", height=1, width=4,
                              command=animacion).place(x=10, y=563)
        ventana.focus_force()
        ventana.mainloop()
        return self.valor

#x=ActualizarPrecio()
#x.vistaActualizar()