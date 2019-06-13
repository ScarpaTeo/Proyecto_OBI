import sys
sys.path.append('../modelos')
sys.path.append('../vista')
import Principal
import loginModel

class ginController():
    def validarUsuario(self,user,passw):
        modelo=loginModel.LoginModel()
        validacion=modelo.validarUsuarioModel(user,passw)
        
        if(validacion==True):
            prin=Principal.Principal()
            prin.cargar()
        else:
            pass
