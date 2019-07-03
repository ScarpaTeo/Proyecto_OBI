import sys
class LoginModel():

    def validarUsuarioModel(self,user,passw):
        usuario="nicolas"
        contrasena="123"
        if(user==usuario and passw==contrasena):
            return True
        else:
            return False

