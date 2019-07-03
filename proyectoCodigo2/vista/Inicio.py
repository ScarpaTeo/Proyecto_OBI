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

        def cerrar():
            'funcion que cierra la app'
            sys.exit()

        ventana=Tk()
        ventana.title("Log In")
        ventana.geometry('700x600+350+0')
        ventana.resizable(width=False,height=False)
        
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
        bt_enter = Button(ventana, text="Ingresar", fg="black", bg="#FFDE00", command=validar, relief="flat", height=2,
                          width=14).place(x=212, y=445)
        bt_cancelar = Button(ventana, text="Cancel", fg="black", bg="#FFFFFF", relief="flat", height=2, width=14,
                             command=cerrar).place(x=404, y=445)

        ventana.mainloop()
        return self.datos




#x=Login()
#x.Motrar()
