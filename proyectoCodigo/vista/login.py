from tkinter import *

class Login():
    def cargar(self):
        ventana=Tk()
        ventana.title("Log In")
        ventana.geometry('395x268')
        img = PhotoImage(file="../imagenes/imgLogin.png")
        Limagen = Label(ventana, image=img).pack()
        Ltitulo=Label(ventana, text="OWNER BUIDER INTEGRATIVE", fg="red" ,font = ( "Helvetica" , 15)).place(x=45,y=140)
        
        #label y campo user
        Luser=Label(ventana,text="User:").place(x=52, y=170)
        user=Entry(ventana, width=35)
        user.place(x=98, y=170)
        Lcontrasena=Label(ventana,text="Password:").place(x=20, y=200)
        contrasena=Entry(ventana,show="*" ,width=35)
        contrasena.place(x=98, y=200)
        #botones enter y cancelar
        bt_enter=Button(ventana, text="Enter").place(x=321,y=230)
        bt_cancelar=Button(ventana, text="Cancel").place(x=230,y=230)
        ventana.mainloop()

lo=Login()
lo.cargar()