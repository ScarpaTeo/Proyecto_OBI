import sys
sys.path.append('../conexion')
from Clase_ConsultaBD import Conexion
class RegitroModel():

    def registrar(self,datos):
        
        sql="INSERT INTO usuario(usuario,contraseña,confirmar_contraseña,email,nombre_completo) VALUES (%s,%s,%s,%s,%s)"
        valores=(datos['usuario'],datos['contraseña'],datos['confirmar_contraseña'],datos['email'],datos['nombre_completo'])
        nuevo=Conexion()
        guardo=nuevo.ejecutar_set(sql,valores)
        if guardo==True:
            return "Se registro el nuevo usuario"
        else:
            return "Error al querer registrar"