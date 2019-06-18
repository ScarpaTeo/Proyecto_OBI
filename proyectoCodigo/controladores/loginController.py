import sys
sys.path.append('../vista')
sys.path.append('../modelos')
from loginModel import LoginModel
from Inicio import Login
from Principal import Principal
class loginController():

    def validarUsuario(self):
        modelo=LoginModel()
        lo=Login()
        datos = lo.Motrar()
        validacion=modelo.validarUsuarioModel(datos['user'],datos['pass'])
        if(validacion==True):
            return True;
        else:
            return False

x = loginController()
print(x.validarUsuario())