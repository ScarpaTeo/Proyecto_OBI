import sys
sys.path.append('../vista')
from tkinter import *
class Login():
    def __init__(self):
        self.datos = None
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
            self.datos="Registro"
            ventana.destroy()

        def pressEnter(evento):
            validar()

        ventana=Tk()
        ventana.title("Log In")
        ventana.geometry('700x600+350+0')
        ventana.resizable(width=False,height=False)
        ventana.bind("<Return>",pressEnter)

        #----------- imagen de fondo
        icono=PhotoImage(file="../imagenes/log2.png")
        Limg=Label(ventana,image=icono).pack()
        
        #------------- campo user
        self.user=Entry(ventana, width=16,relief="flat",bg="#FEE780",font=('Arial',18))
        self.user.place(x=253, y=281)
        self.user.focus()
        #-----------campo contrasena
        self.contrasena=Entry(ventana,show="*" ,width=16,relief="flat",bg="#FEE780",font=('Arial',18))
        self.contrasena.place(x=253 ,y=373)

        #--------------- botones enter y cancelar
        bt_enter = Button(ventana, text="Ingresar", fg="black", bg="#FFDE00", command=validar, relief="flat", height=2,
                          width=14).place(x=209, y=448)#FFFFFF
        bt_registrar = Button(ventana, text="Registrarse", fg="black", bg="#FFFFFF", relief="flat", height=2, width=14,
                              command=registrarse).place(x=402, y=448)

      #  bt_ayuda = Button(ventana, text="Ayuda", fg="#FFDE00", bg="#1E1E1E", relief="flat", height=1, width=4,
       #                       command=animacion).place(x=10, y=563)

        ventana.focus_force()
        ventana.mainloop()
        return self.datos

#x=Login()
#x.Motrar()