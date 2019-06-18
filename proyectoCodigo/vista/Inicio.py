import sys
sys.path.append('../vista')
from tkinter import *
class Login():
    def __init__(self):
        self.datos = None
    def Motrar(self):
        
        ventana=Tk()
        ventana.title("Log In")
        ventana.geometry('430x410')
        ventana.resizable(width=False,height=False)
        
        #icono
        icono=PhotoImage(file="../imagenes/casco.png")
        Limg=Label(ventana,image=icono).pack()
        
        #label y campo user
        Luser=Label(ventana,text="Usuario",font=("Arial",20)).place(x=162, y=230)
        self.user=Entry(ventana, width=45)
        self.user.place(x=35, y=265)

        #label y campo contrasena
        Lcontrasena=Label(ventana,text="Contrasena",font=("Arial",20)).place(x=143, y=300)        
        self.contrasena=Entry(ventana,show="*" ,width=45)
        self.contrasena.place(x=35, y=335)
        def validar():
            usuario=str(self.user.get())
            password=str(self.contrasena.get())
            ventana.destroy()
            self.datos={
                "user":usuario,
                "pass":password
            }
            return self.datos
        #botones enter y cancelar
        bt_enter=Button(ventana, text="Ingresar", fg="black", bg="#04B404",command=validar).place(x=320,y=368)
        bt_cancelar=Button(ventana, text="Cancel", fg="black", bg="red").place(x=230,y=368)
        
        ventana.mainloop()
        return self.datos

