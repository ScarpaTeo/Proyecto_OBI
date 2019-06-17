import sys
sys.path.append('../vista')
sys.path.append('../modelos')
from loginModel import LoginModel

class loginController():
    def validarUsuario(self,user,passw):
        modelo=LoginModel()
        validacion=modelo.validarUsuarioModel(user,passw)
        if(validacion==True):
            return True;
        else:
            return False
