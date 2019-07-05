import sys
sys.path.append('../conexion')
from Clase_ConsultaBD import Conexion
class actualizarLosPrecioModel():
    def __init__(self):
        self.dato=""
    def actualizarPrecioMateriales(self,tipo,precio):
        sql3="UPDATE materiales SET precio=%s WHERE tipo=%s ;"
        datos=(precio,tipo)
        actualizar=Conexion()
        actualizar.ejecutar_set(sql3,datos)
        return "Se actualizo el precio del material"
    
    def obtenerPrecios(self):
        sql4="SELECT * FROM materiales"
        traer=Conexion()
        dato=traer.ejecutar_get(sql4)
        self.dato=dato


#x=actualizarLosPrecioModel()
#x.obtenerPrecios()
#print(x.dato)