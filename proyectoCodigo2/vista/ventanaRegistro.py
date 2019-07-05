from tkinter import *
class Registro():

        def __init__(self):
            self.datos=None
        def mostrarRegistro(self,resultado=""):
            def errorVacio():
                error.config(text="Error!, todos los campos deben estar completos!")
            #-------------------Seccion ventana
            ventana=Tk()
            ventana.title("Registro")
            ventana.geometry("700x585+350+50")
            ventana.resizable(width=False,height=False)

            #-------------------imagen de fondo
            icono=PhotoImage(file="../imagenes/Registro.png")
            img=Label(ventana,image=icono).pack()
            error=Label(ventana,text="",bg="#fff",fg="red",font=("Arial",11))
            error.place(x=200, y=488)
            guardado=Label(ventana,text=resultado,bg="#fff",fg="black",font=("Arial",11))
            guardado.place(x=260, y=488)


            def validar():
                #funcion para validar los datos
               if not self.name.get() or not self.user.get() or not self.email.get() or not self.contrasena.get() or not self.confirm_contrasena.get():
                   errorVacio()
               else:
                   nombre_completo = str(self.name.get())
                   usuario = str(self.user.get())
                   email = str(self.email.get())
                   password = str(self.contrasena.get())
                   confirm_pass = str(self.confirm_contrasena.get())

                   self.datos = {
                        "nombre_completo":nombre_completo,
                        "usuario":usuario,
                        "email":email,
                        "contraseña":password,
                        "confirmar_contraseña":confirm_pass
                   }
                   ventana.destroy()

            def volverLogin():
            #cierra la ventana y vuelve al menu de login
                ventana.destroy()
                self.datos = "Login"

            #-------------------seccion de entrys
            self.name=Entry(ventana,width=33,relief="flat",bg="#FEE780",font=('Arial',16))
            self.name.place(x=158, y=78)

            self.user=Entry(ventana,width=33,relief="flat",bg="#FEE780",font=('Arial',16))
            self.user.place(x=158, y=171)

            self.email=Entry(ventana,width=33,relief="flat",bg="#FEE780",font=('Arial',16))
            self.email.place(x=158, y=264)

            self.contrasena=Entry(ventana,show="*",width=33,relief="flat",bg="#FEE780",font=('Arial',16))
            self.contrasena.place(x=158, y=357)

            self.confirm_contrasena=Entry(ventana,show="*",width=33,relief="flat",bg="#FEE780",font=('Arial',16))
            self.confirm_contrasena.place(x=158, y=448)
            #-------------------seccion botones
            bt_register = Button(ventana, text="Registrar", fg="black", bg="#FEE780", command=validar, relief="flat", height=2,
                          width=13,font=('Arial',11)).place(x=215, y=522)
            bt_cancelar = Button(ventana, text="Atras", fg="black", bg="#FFFFFF", command=volverLogin, relief="flat", height=2,
                          width=13,font=('Arial',11)).place(x=387, y=522)

            ventana.mainloop()
            return self.datos