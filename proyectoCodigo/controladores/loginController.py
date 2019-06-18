import sys
sys.path.append('../vista')
sys.path.append('../modelos')
from loginModel import LoginModel
from Inicio import Login
from Principal import Principal
from Error_Usuario import ErrorUsuario
class loginController():
    
    def validarUsuario(self):
        modelo=LoginModel()
        lo=Login()
        datos = lo.Motrar()
        validacion=modelo.validarUsuarioModel(datos['user'],datos['pass'])
        if(validacion==True):
            pri=Principal()
            print(pri.mostrar())
        else:
            err=ErrorUsuario()
x = loginController()
print(x.validarUsuario())