from tkinter import *
import tkinter.ttk as ttk
# import sys
# sys.path.append('../calculos')
# from calculo import *
class calculo():

    #ventana para el calculo de cimiento
    def cimiento(self):
        def calculoCimiento():
            alto=float(Calto.get())
            ancho=float(Cancho.get())
            profundidad=float(Cprofundidad.get())
            valor=str(Ctipo.get())

            if valor=="pilotin":
                print("es un pilotin")
            elif valor=="Corrida":
                print("es una corrida")
            elif valor=="viga":
                print("es una viga")

            

        ventana=Tk()
        ventana.title('Calcular Cimiento')
        ventana.geometry('300x300')
        img=PhotoImage(file="../imagenes/pala.png")
        Licono=Label(ventana,image=img).pack()

        Lalto=Label(ventana,text="Alto:",font=('Arial',18)).place(x=122,y=80)
        Calto=Entry(ventana,width=30)
        Calto.place(x=28,y=110)

        Lancho=Label(ventana,text="Ancho:",font=('Arial',18)).place(x=110,y=140)
        Cancho=Entry(ventana,width=30)
        Cancho.place(x=28,y=170)

        Lprofundidad=Label(ventana,text="Profundidad:",font=('Arial',18)).place(x=81,y=199)
        Cprofundidad=Entry(ventana,width=30)
        Cprofundidad.place(x=28,y=230)

        Ctipo = ttk.Combobox(values=["Corrida", "viga", "pilotin"])
        # cbx.set("uno")
        Ctipo.configure(width=29)
        Ctipo.place(x=28,y=250)

        BcalcularCimiento=Button(ventana,text="Calcular",command=calculoCimiento).place(x=109,y=260)
        ventana.mainloop()
    
    #ventana para el calculo de contrapiso
    def contrapiso(self):
        ventana=Tk()
        ventana.title('Calcular Contrapiso')
        ventana.geometry('300x300')
        img=PhotoImage(file="../imagenes/pala.png")
        Licono=Label(ventana,image=img).pack()

        Llargo=Label(ventana,text="Largo:",font=('Arial',18)).place(x=120,y=80)
        Clargo=Entry(ventana,width=30)
        Clargo.place(x=28,y=110)

        Lancho=Label(ventana,text="Ancho:",font=('Arial',18)).place(x=116,y=140)
        Cancho=Entry(ventana,width=30)
        Cancho.place(x=28,y=170)

        Lespesor=Label(ventana,text="Espesor:",font=('Arial',18)).place(x=106,y=199)
        Cespersor=Entry(ventana,width=30)
        Cespersor.place(x=28,y=230)

        BcalcularCimiento=Button(ventana,text="Calcular").place(x=114,y=260)
        ventana.mainloop()
    
    #ventana para el calculo de pared
    def pared(self):
        ventana=Tk()
        ventana.title('Calcular Pared')
        ventana.geometry('300x245')
        img=PhotoImage(file="../imagenes/pala.png")
        Licono=Label(ventana,image=img).pack()

        Llargo=Label(ventana,text="Largo:",font=('Arial',18)).place(x=120,y=80)
        Clargo=Entry(ventana,width=30)
        Clargo.place(x=28,y=110)

        Lancho=Label(ventana,text="Alto:",font=('Arial',18)).place(x=128,y=140)
        Cancho=Entry(ventana,width=30)
        Cancho.place(x=28,y=170)

        BcalcularCimiento=Button(ventana,text="Calcular").place(x=113,y=200)
        ventana.mainloop()
    
    def revoque(self):
        ventana=Tk()
        ventana.title('Calcular Revoque')
        ventana.geometry('300x245')
        img=PhotoImage(file="../imagenes/pala.png")
        Licono=Label(ventana,image=img).pack()

        Llargo=Label(ventana,text="Largo:",font=('Arial',18)).place(x=120,y=80)
        Clargo=Entry(ventana,width=30)
        Clargo.place(x=28,y=110)

        Lancho=Label(ventana,text="Alto:",font=('Arial',18)).place(x=128,y=140)
        Cancho=Entry(ventana,width=30)
        Cancho.place(x=28,y=170)

        BcalcularCimiento=Button(ventana,text="Calcular").place(x=113,y=200)
        ventana.mainloop()