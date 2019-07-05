import sys
sys.path.append('../conexion')
from Clase_ConsultaBD import Conexion
class LoginModel():

    def validarUsuarioModel(self,user,passw):
        #consulta
        sql2="SELECT * FROM usuario WHERE usuario='{0}' AND contraseña={1}".format(user,passw)
        #conexion
        nueva=Conexion()
        #se ejecuta el get y se traen los datos retornados cono un tupla dentro de un arreglo
        datos=nueva.ejecutar_get(sql2)
        #se verifica si trae al menos un dato sino ya se retorna false
        if not datos:
        #a la variable datos se le reaccigna la tupla para poder tratar los datos
            return False
        else:
            datos=datos[0]
            #condicion de si es valido los datos
            if(user==datos[1] and passw==datos[2]):
                return True
            else:
                return False

