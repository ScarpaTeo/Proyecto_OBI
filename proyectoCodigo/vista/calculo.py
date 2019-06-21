# esto sirve para insertar por lineas en los textfield en el Tkinter
#T.insert(tk.END, "Just a text Widget\nin two lines\n")

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
        ventana.geometry('543x420')
        img=PhotoImage(file="../imagenes/pala.png")
        Licono=Label(ventana,image=img).pack()

        #--------------combo box
        Lcombo=Label(ventana,text="Elige uno:",font=('Arial',12)).place(x=28,y=85)
        Ccombo = ttk.Combobox(values=["Corrida", "viga", "pilotin"],state="readonly")
        print(Ccombo.get())
        Ccombo.configure(width=29)
        Ccombo.place(x=28,y=110)

        #--------------------campo y label Alto
        Lalto=Label(ventana,text="Alto:",font=('Arial',12)).place(x=28,y=145)
        Calto=Entry(ventana,width=30)
        Calto.place(x=28,y=170)

        #-------------------campo y laber ancho
        Lancho=Label(ventana,text="Ancho:",font=('Arial',12)).place(x=28,y=205)
        Cancho=Entry(ventana,width=30)
        Cancho.place(x=28,y=230)

        #---------------campo y label profundidad
        Lprofundidad=Label(ventana,text="Profundidad:",font=('Arial',12)).place(x=28,y=265)
        Cprofundidad=Entry(ventana,width=30)
        Cprofundidad.place(x=28,y=290)

        #------------------------Text field
        LtextField=Label(ventana,text="Detalle de Materiales ",font=('Arial',18)).place(x=265,y=110)
        Dtextfiel=Text(ventana, height=15, width=30).place(x=260 ,y=145)

        #---------boton calcular
        BcalcularCimiento=Button(ventana, height=3, width=28,text="Calcular",command=calculoCimiento).place(x=28,y=335)
        ventana.mainloop()
    
    #ventana para el calculo de contrapiso
    def contrapiso(self):

        def calculoContrapiso():
            alto=float(Calto.get())
            ancho=float(Cancho.get())
            profundidad=float(Cprofundidad.get())
            valor=str(Ctipo.get())


        ventana=Tk()
        ventana.title('Calcular Contrapiso')
        ventana.geometry('543x420')
        img=PhotoImage(file="../imagenes/pala.png")
        Licono=Label(ventana,image=img).pack()

        #--------------------campo y label Alto
        Lalto=Label(ventana,text="Alto:",font=('Arial',12)).place(x=28,y=145)
        Calto=Entry(ventana,width=30)
        Calto.place(x=28,y=170)

        #-------------------campo y laber ancho
        Lancho=Label(ventana,text="Ancho:",font=('Arial',12)).place(x=28,y=205)
        Cancho=Entry(ventana,width=30)
        Cancho.place(x=28,y=230)

        #---------------campo y label profundidad
        Lprofundidad=Label(ventana,text="Profundidad:",font=('Arial',12)).place(x=28,y=265)
        Cprofundidad=Entry(ventana,width=30)
        Cprofundidad.place(x=28,y=290)

        #------------------------Text field
        LtextField=Label(ventana,text="Detalle de Materiales ",font=('Arial',18)).place(x=265,y=110)
        Dtextfiel=Text(ventana, height=15, width=30).place(x=260 ,y=145)

        #---------boton calcular
        BcalcularCimiento=Button(ventana, height=3, width=28,text="Calcular",command=calculoContrapiso).place(x=28,y=335)
        ventana.mainloop()


    #ventana para el calculo de pared
    def pared(self):

        def calculoPared():
            alto=float(Calto.get())
            ancho=float(Cancho.get())
            tipo=str(Ccombo.get())
            espesor=str(Cespesor.get())


        ventana=Tk()
        ventana.title('Calcular Pared')
        ventana.geometry('543x420')
        img=PhotoImage(file="../imagenes/pala.png")
        Licono=Label(ventana,image=img).pack()

        #--------------combo box tipo de pared
        Lcombo=Label(ventana,text="Elige uno:",font=('Arial',12)).place(x=28,y=85)
        Ccombo = ttk.Combobox(values=["Pared de Bloques", "Pared de Tabiques", "Pared Común"],state="readonly")
        Ccombo.configure(width=29)
        Ccombo.place(x=28,y=110)
        #--------------------campo y label Alto
        Lalto=Label(ventana,text="Alto:",font=('Arial',12)).place(x=28,y=145)
        Calto=Entry(ventana,width=30)
        Calto.place(x=28,y=170)

        #-------------------campo y laber ancho
        Lancho=Label(ventana,text="Ancho:",font=('Arial',12)).place(x=28,y=205)
        Cancho=Entry(ventana,width=30)
        Cancho.place(x=28,y=230)

        #---------------combox y label espesor
        Lespesor = Label(ventana, text="seleccione el Espesor:", font=('Arial', 12)).place(x=28, y=265)
        Cespesor= ttk.Combobox(values=["0.15 cm", "0.20 cm", "0.30 cm"],state="readonly")
        Cespesor.configure(width=10)
        Cespesor.place(x=28,y=295)

        #------------------------Text field
        LtextField=Label(ventana,text="Detalle de Materiales ",font=('Arial',18)).place(x=265,y=110)
        Dtextfiel=Text(ventana, height=15, width=30).place(x=260 ,y=145)

        #---------boton calcular
        BcalcularCimiento=Button(ventana, height=3, width=28,text="Calcular",command=calculoPared).place(x=28,y=335)
        ventana.mainloop()

    def revoque(self):

        def calculoRevoque():
            alto=float(Calto.get())
            ancho=float(Cancho.get())
            tipo=str(Ccombo.get())


        ventana=Tk()
        ventana.title('Calcular Reboques')
        ventana.geometry('543x420')
        img=PhotoImage(file="../imagenes/pala.png")
        Licono=Label(ventana,image=img).pack()

        #--------------combo box tipo de pared
        Lcombo=Label(ventana,text="Elige uno:",font=('Arial',12)).place(x=28,y=85)
        Ccombo = ttk.Combobox(values=["Revoque Impearmeable", "Reboque Grueso", "Reboque fino"],state="readonly")
        Ccombo.configure(width=29)
        Ccombo.place(x=28,y=110)
        #--------------------campo y label Alto
        Lalto=Label(ventana,text="Alto:",font=('Arial',12)).place(x=28,y=145)
        Calto=Entry(ventana,width=30)
        Calto.place(x=28,y=170)

        #-------------------campo y laber ancho
        Lancho=Label(ventana,text="Ancho:",font=('Arial',12)).place(x=28,y=205)
        Cancho=Entry(ventana,width=30)
        Cancho.place(x=28,y=230)

        #------------------------Text field
        LtextField=Label(ventana,text="Detalle de Materiales ",font=('Arial',18)).place(x=265,y=110)
        Dtextfiel=Text(ventana, height=15, width=30).place(x=260 ,y=145)

        #---------boton calcular
        BcalcularCimiento=Button(ventana, height=3, width=28,text="Calcular",command=calculoRevoque).place(x=28,y=335)
        ventana.mainloop()
    def techo(self):

        def calculoTecho():
            alto=float(Calto.get())
            ancho=float(Cancho.get())
            tipo=str(Ccombo.get())


        ventana=Tk()
        ventana.title('Calcular de Techo')
        ventana.geometry('543x420')
        img=PhotoImage(file="../imagenes/pala.png")
        Licono=Label(ventana,image=img).pack()

        #--------------combo box tipo de pared
        Lcombo=Label(ventana,text="Largo de Chapa:",font=('Arial',12)).place(x=28,y=85)
        Ccombo = ttk.Combobox(values=["1.83","2.13","2.44","2.74","3.05","3.36","3.66","3.96"],state="readonly")
        Ccombo.configure(width=29)
        Ccombo.place(x=28,y=110)
        #--------------------campo y label Alto
        Lalto=Label(ventana,text="Largo:",font=('Arial',12)).place(x=28,y=145)
        Calto=Entry(ventana,width=30)
        Calto.place(x=28,y=170)

        #-------------------campo y laber ancho
        Lancho=Label(ventana,text="Ancho:",font=('Arial',12)).place(x=28,y=205)
        Cancho=Entry(ventana,width=30)
        Cancho.place(x=28,y=230)

        #------------------------Text field
        LtextField=Label(ventana,text="Detalle de Materiales ",font=('Arial',18)).place(x=265,y=110)
        Dtextfiel=Text(ventana, height=15, width=30).place(x=260 ,y=145)

        #---------boton calcular
        BcalcularCimiento=Button(ventana, height=3, width=28,text="Calcular",command=calculoTecho).place(x=28,y=335)
        ventana.mainloop()



