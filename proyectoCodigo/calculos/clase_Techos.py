#clase calculo de techos-------------------------------------
class Techos_calculo:
    def __init__(self,largo,ancho,chapa):
        self.largo=largo
        self.ancho=ancho
        self.chapa=chapa
        self.detalle=[]

    def calculo_techo(self):
        'Cantidad de chapas necesarias'
        y=self.largo*self.ancho
        cantidad=round(y/self.chapa,2)
        self.detalle.append(cantidad)

    def calculo_correas(self):
        'cantidad de tirantes o correas necesarias para el techo '
        maximo=max(self.largo,self.ancho)
        separacion=float(input("ingrese la separacion entre tirantes"))
        dato=round(maximo-separacion*2,2)
        total=round(dato/separacion,2)+2
        self.detalle.append(total)
#---------------------------------------------------------------
#n=Techos(20,10)
#n.calculo_correas()