from tkinter import *
class Registro():

        def __init__(self):
            self.datos=None
        def mostrarRegistro(self,resultado=""):
            def errorVacio():
                error.config(text="Error!, todos los campos deben estar completos!")
            def errorContraseñas():
                error.config(text="Error!, Las contraseñas no coinciden!")
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
                   if self.contrasena.get()==self.confirm_contrasena.get():
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
                   else:
                         errorContraseñas()

            def volverLogin():
            #cierra la ventana y vuelve al menu de login
                ventana.destroy()
                self.datos = "Login"
            def animacion():
                pass

            #-------------------seccion de entrys
            self.name=Entry(ventana,width=32,relief="flat",bg="#FFFFFF",font=('Arial',16))
            self.name.place(x=166, y=78)

            self.user=Entry(ventana,width=32,relief="flat",bg="#FFFFFF",font=('Arial',16))
            self.user.place(x=166, y=171)

            self.email=Entry(ventana,width=32,relief="flat",bg="#FFFFFF",font=('Arial',16))
            self.email.place(x=166, y=264)

            self.contrasena=Entry(ventana,show="*",width=32,relief="flat",bg="#FFFFFF",font=('Arial',16))
            self.contrasena.place(x=166, y=357)

            self.confirm_contrasena=Entry(ventana,show="*",width=32,relief="flat",bg="#FFFFFF",font=('Arial',16))
            self.confirm_contrasena.place(x=166, y=448)
            #-------------------seccion botones
            bt_register = Button(ventana, text="Registrar", fg="black",activebackground="#FFDE00",bg="#FFDE00", command=validar, relief="flat", height=2,
                          width=13,font=('Arial',11)).place(x=215, y=522)
            bt_cancelar = Button(ventana, text="Atras", fg="black",activebackground="#FFFFFF", bg="#FFFFFF", command=volverLogin, relief="flat", height=2,
                          width=13,font=('Arial',9)).place(x=401, y=522)
            bt_ayuda = Button(ventana, text="Ayuda",command=animacion ,fg="#FFDE00",activebackground="#1E1E1E",bg="#1E1E1E", relief="flat", height=1,
                              width=4).place(x=10, y=557)

            ventana.mainloop()
            return self.datos


#x=Registro()
#x.mostrarRegistro()