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
        BcalcularCimiento=Button(ventana,width=11,relief="flat",bg="#FFDE00",font=('Arial',18),text="Calcular",command=calculoCimiento).place(x=131,y=454)

        # ---------boton atras
        Batras=Button(ventana,width=4,relief="flat",bg="#FFFFFF",font=('Arial',16),text="Atras").place(x=518,y=89)

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
        BcalcularCimiento=Button(ventana,width=11,relief="flat",bg="#FFDE00",font=('Arial',18),text="Calcular",command=calculoContrapiso).place(x=131,y=454)

        # ---------boton atras
        Batras=Button(ventana,width=4,relief="flat",bg="#FFFFFF",font=('Arial',16),text="Atras").place(x=518,y=89)
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
        ventana.geometry('700x600')
        img=PhotoImage(file="../imagenes/pared.png")
        Licono=Label(ventana,image=img).pack()

        #--------------combo box tipo de pared
        Ccombo = ttk.Combobox(values=["Pared de Bloques", "Pared de Tabiques", "Pared Común"],state="readonly",font=('Arial',12))
        Ccombo.configure(width=16)
        Ccombo.place(x=128,y=140)
        #--------------------campo Alto
        Calto=Entry(ventana,width=14,relief="flat",bg="#FEE780",font=('Arial',16))
        Calto.place(x=128,y=220)

        #-------------------campo ancho
        Cancho=Entry(ventana,width=14,relief="flat",bg="#FEE780",font=('Arial',16))
        Cancho.place(x=128,y=304)

        #---------------combox espesor
        Cespesor= ttk.Combobox(values=["0.15 cm", "0.20 cm", "0.30 cm"],state="readonly",font=('Arial',11))
        Cespesor.configure(width=9)
        Cespesor.place(x=128,y=390)

        #------------------------Text field
        Dtextfiel=Text(ventana,width=21,height=13,relief="flat",bg="#FFFFFF",font=('Arial',18)).place(x=316 ,y=150)

        #---------boton calcular
        BcalcularCimiento=Button(ventana,width=11,relief="flat",bg="#FFDE00",font=('Arial',18),text="Calcular",command=calculoPared).place(x=131,y=454)

        #--------boton atras
        Batras=Button(ventana,width=4,relief="flat",bg="#FFFFFF",font=('Arial',16),text="Atras").place(x=518,y=89)
        ventana.mainloop()

    def revoque(self):

        def calculoRevoque():
            alto=float(Calto.get())
            ancho=float(Cancho.get())
            tipo=str(Ccombo.get())


        ventana=Tk()
        ventana.title('Calcular Reboques')
        ventana.geometry('700x600')
        img=PhotoImage(file="../imagenes/revoque.png")
        Licono=Label(ventana,image=img).pack()

        #--------------combo box tipo de pared
        Ccombo = ttk.Combobox(values=["Revoque Impearmeable", "Reboque Grueso", "Reboque fino"],state="readonly",font=('Arial',12))
        Ccombo.configure(width=16)
        Ccombo.place(x=128,y=168)
        #--------------------campo Alto
        Calto=Entry(ventana,width=14,relief="flat",bg="#FEE780",font=('Arial',16))
        Calto.place(x=128,y=249)

        #-------------------campo ancho
        Cancho=Entry(ventana,width=14,relief="flat",bg="#FEE780",font=('Arial',16))
        Cancho.place(x=128,y=332)

        #------------------------Text field
        Dtextfiel=Text(ventana,width=21,height=13,relief="flat",bg="#FFFFFF",font=('Arial',18)).place(x=316 ,y=150)

        #---------boton calcular
        BcalcularCimiento=Button(ventana,width=11,relief="flat",bg="#FFDE00",font=('Arial',18),text="Calcular",command=calculoRevoque).place(x=131,y=454)

        #--------boton atras
        Batras=Button(ventana,width=4,relief="flat",bg="#FFFFFF",font=('Arial',16),text="Atras").place(x=518,y=89)
        ventana.mainloop()
    def techo(self):

        def calculoTecho():
            alto=float(Calto.get())
            ancho=float(Cancho.get())
            tipo=str(Ccombo.get())


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
        Dtextfiel=Text(ventana,width=21,height=13,relief="flat",bg="#FFFFFF",font=('Arial',18)).place(x=316 ,y=150)

        #---------boton calcular
        BcalcularCimiento=Button(ventana,width=11,relief="flat",bg="#FFDE00",font=('Arial',18),text="Calcular",command=calculoTecho).place(x=131,y=454)

        #--------boton atras
        Batras=Button(ventana,width=4,relief="flat",bg="#FFFFFF",font=('Arial',16),text="Atras").place(x=518,y=89)
        ventana.mainloop()



#x=calculo()
#x.techo()
#x.cimiento()
#x.pared()
#x.contrapiso()
#x.revoque()