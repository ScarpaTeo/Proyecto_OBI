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
        ventana.geometry('950x650')
        ventana.resizable(width=False,height=False)
        img = PhotoImage(file="../imagenes/MenuLogin.png")
        Limagen = Label(ventana, image=img).pack(fill = BOTH, expand=1)
        #label y campo user
        user=Entry(ventana, width=35)
        user.place(x=350, y=370)
        contrasena=Entry(ventana,show="*" ,width=35)
        contrasena.place(x=350, y=440)
        #botones enter y cancelar
        bt_enter=Button(ventana, text="Enter", command=validar).place(x=573,y=475)
        bt_cancelar=Button(ventana, text="Cancel").place(x=490,y=475)
        ventana.mainloop()

lo=Login()
lo.cargar()