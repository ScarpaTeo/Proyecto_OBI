from tkinter import *

class calculo():
    def cargar(self):
        ventana=Tk()
        ventana.geometry('400x300')
        ventana.title('calculo')
        ventana.resizable(width=False,height=False)
        img = PhotoImage(file="../imagenes/fondo.png")
        Limagen = Label(ventana, image=img).pack(fill = BOTH, expand=1)
        la=Label(ventana,text="pruebaasdasdasdasd")
        la.place(x=10,y=20)
        ventana.mainloop()

cal=calculo()
cal.cargar()
