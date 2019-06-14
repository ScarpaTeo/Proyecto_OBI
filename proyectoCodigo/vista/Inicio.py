from tkinter import *
import sys
sys.path.append('../controladores')
from loginController import ginController
class Login():
    def cargar(self):
        
        def validar():
            usuario=str(user.get())
            password=str(contrasena.get())
            con=ginController()
            con.validarUsuario(usuario,password)
        ventana=Tk()
        ventana.title("Log In")
        ventana.geometry('900x600')
        ventana.resizable(width=False,height=False)
        img = PhotoImage(file="../imagenes/fondo.png")
        Limagen = Label(ventana, image=img).pack(fill = BOTH, expand=1)
        #label y campo user
        Luser=Label(ventana,text="User:").place(x=52, y=170)
        user=Entry(ventana, width=35)
        user.place(x=98, y=170)
        Lcontrasena=Label(ventana,text="Password:").place(x=20, y=200)
        contrasena=Entry(ventana,show="*" ,width=35)
        contrasena.place(x=98, y=200)
        #botones enter y cancelar
        bt_enter=Button(ventana, text="Enter", command=validar).place(x=321,y=230)
        bt_cancelar=Button(ventana, text="Cancel").place(x=230,y=230)
        ventana.mainloop()

lo=Login()
lo.cargar()