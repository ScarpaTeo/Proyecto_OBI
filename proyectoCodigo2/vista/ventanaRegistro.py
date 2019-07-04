from tkinter import *
class Registro():

        def __init__(self):
            self.datos=None
            self.valor=None
        def mostrarRegistro(self):
            def validar():
                #funcion para validar los datos 
               nombre_completo = str(self.name.get())
               usuario = str(self.user.get())
               email = str(self.email.get())
               password = str(self.contrasena.get())
               confirm_pass = str(self.confirm_pass.get())
            
               self.datos = {
                   "name":nombre_completo,
                   "user":usuario,
                   "email":email,
                   "contrasena":password,
                   "confirm_pass":confirm_pass
               }
               ventana.destroy()

            def nuevoRegistro():
            #cierra la ventana luego del nuevo registro
                self.valor="Registrar"
                ventana.destroy()

            def volverLogin():
            #cierra la ventana y vuelve al menu de login
                ventana.destroy()
                self.valor = "Principal"

            #-------------------Seccion ventana
            ventana=Tk()
            ventana.title("Registro")
            ventana.geometry("700x585+350+50")
            ventana.resizable(width=False,height=False)

            #-------------------imagen de fondo
            icono=PhotoImage(file="../imagenes/Registro.png")
            img=Label(ventana,image=icono).pack()

            #-------------------seccion de entrys
            self.name=Entry(ventana,width=33,relief="flat",bg="#FEE780",font=('Arial',16))
            self.name.place(x=158, y=78)

            self.user=Entry(ventana,width=33,relief="flat",bg="#FEE780",font=('Arial',16))
            self.user.place(x=158, y=171)

            self.email=Entry(ventana,width=33,relief="flat",bg="#FEE780",font=('Arial',16))
            self.email.place(x=158, y=264)

            self.contrasena=Entry(ventana,width=33,relief="flat",bg="#FEE780",font=('Arial',16))
            self.contrasena.place(x=158, y=357)

            self.confirm_contrasena=Entry(ventana,width=33,relief="flat",bg="#FEE780",font=('Arial',16))
            self.confirm_contrasena.place(x=158, y=448)
            #-------------------seccion botones
            bt_register = Button(ventana, text="Registrar", fg="black", bg="#FEE780", command=validar, relief="flat", height=2,
                          width=13,font=('Arial',11)).place(x=215, y=522)
            bt_cancelar = Button(ventana, text="Cancelar", fg="black", bg="#FFFFFF", command=validar, relief="flat", height=2,
                          width=13,font=('Arial',11)).place(x=387, y=522)

            ventana.mainloop()