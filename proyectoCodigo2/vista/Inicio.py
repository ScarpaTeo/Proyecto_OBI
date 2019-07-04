import sys
sys.path.append('../vista')
from tkinter import *
class Login():

    def __init__(self):
        self.datos = None
        self.valor=None
    def Motrar(self):

        def validar():
            'funcion obtiene el valor de los campos'
            usuario = str(self.user.get())
            password = str(self.contrasena.get())
            
            self.datos = {
                "user": usuario,
                "pass": password
            }
            ventana.destroy()

        def registrarse():
            'funcion que cierra la app'
            self.valor="Registro"
            ventana.destroy()

        ventana=Tk()
        ventana.title("Log In")
        ventana.geometry('700x600+350+0')
        ventana.resizable(width=False,height=False)
        top = Frame(ventana)
        top.pack()

        
        #----------- imagen de fondo
        icono=PhotoImage(file="../imagenes/log2.png")
        Limg=Label(ventana,image=icono).pack()
        
        #------------- campo user
        self.user=Entry(ventana, width=16,relief="flat",bg="#FEE780",font=('Arial',18))
        self.user.place(x=253, y=281)

        #-----------campo contrasena
        self.contrasena=Entry(ventana,show="*" ,width=16,relief="flat",bg="#FEE780",font=('Arial',18))
        self.contrasena.place(x=253 ,y=373)

        #--------------- botones enter y cancelar
        bt_enter = Button(ventana,text="Ingresar", fg="black", bg="#FFDE00", command=validar, relief="flat", height=2,
                          width=14).place(x=212, y=445)
        bt_cancelar = Button(ventana, text="Registrarse", fg="black", bg="#FFFFFF", relief="flat", height=2, width=14,
                             command=registrarse).place(x=404, y=445)
        entry = Entry(top)
        entry.pack()
        bt_enter.pack()


        def onEnter(event):
            funcion()

        def funcion():
             print (entry.get())

        entry.bind('<Return>', onEnter)
        bt_enter.config(command = funcion)


        ventana.mainloop()
        return self.datos





