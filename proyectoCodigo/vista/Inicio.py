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
        ventana.geometry('800x580')
        ventana.resizable(width=False,height=False)
        img = PhotoImage(file="../imagenes/MenuLogin.png")
        Limagen = Label(ventana, image=img).pack(fill = BOTH, expand=1)
        #label y campo user
        user=Entry(ventana, width=35)
        user.place(x=275, y=330)
        contrasena=Entry(ventana,show="*" ,width=35)
        contrasena.place(x=275, y=393)
        #botones enter y cancelar
        bt_enter=Button(ventana, text="Enter",command=validar, fg="black", bg="yellow").place(x=495,y=424)
        bt_cancelar=Button(ventana, text="Cancel", fg="black", bg="red").place(x=408,y=424)
        ventana.mainloop()

lo=Login()
lo.cargar()