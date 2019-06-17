from tkinter import *
import sys
sys.path.append('../controladores')
from loginController import loginController
from Principal import Principal
from Error_Usuario import ErrorUsuario
class Login():
    
    def __init__(self):
        def cerrar():
            ventana.destroy()
            
        #funcion la cual valida el usuario
        def validar():
            #se le pasa usuario y contraseña
            usuario=str(user.get())
            password=str(contrasena.get())
            #se cierra la ventana
            ventana.destroy()
            #se crea un objeto de loginController para usar el metodo para validar usuario
            con=loginController()
            validar=con.validarUsuario(usuario,password)
            #dependiendo que me devuelva validar abro Principal o vuelvo al login y muestro el error
            if validar==True:
                pri=Principal()
            else:
                err=ErrorUsuario()
                lo=Login()
        
        ventana=Tk()
        ventana.title("Log In")
        ventana.geometry('430x410')
        ventana.resizable(width=False,height=False)
        
        #icono
        icono=PhotoImage(file="../imagenes/casco.png")
        Limg=Label(ventana,image=icono).pack()
        
        #label y campo user
        Luser=Label(ventana,text="Usuario",font=("Arial",20)).place(x=162, y=230)
        user=Entry(ventana, width=45)
        user.place(x=35, y=265)

        #label y campo contraseña
        Lcontraseña=Label(ventana,text="Contraseña",font=("Arial",20)).place(x=143, y=300)        
        contrasena=Entry(ventana,show="*" ,width=45)
        contrasena.place(x=35, y=335)

        #botones enter y cancelar
        bt_enter=Button(ventana, text="Ingresar", fg="black", bg="#04B404",command=validar).place(x=320,y=368)
        bt_cancelar=Button(ventana, text="Cancel", fg="black", bg="red",command=cerrar).place(x=230,y=368)
        ventana.mainloop()
        

lo=Login()