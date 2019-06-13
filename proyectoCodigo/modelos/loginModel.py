import sys
sys.path.append('../controladores')
import loginController
class LoginModel():

    def validarUsuarioModel(self,user,passw):
        usuario="nicolas"
        contraseña="123"
        if(user==usuario and passw==contraseña):
            return True
        else:
            return False

