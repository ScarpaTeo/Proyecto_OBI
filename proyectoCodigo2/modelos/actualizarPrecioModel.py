import sys
sys.path.append('../conexion')
from Clase_ConsultaBD import Conexion
class actualizarLosPrecioModel():

    def actualizarPrecioMateriales(self,tipo,precio):
        sql3="UPDATE materiales SET precio=%s WHERE tipo=%s ;"
        datos=(precio,tipo)
        actualizar=Conexion()
        actualizar.ejecutar_set(sql3,datos)
        return "Se actualizo el precio del material"
    
    def obtenerPrecios():
        pass

        