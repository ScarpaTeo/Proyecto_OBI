#clase calculo de techos-------------------------------------
class Techos:
    def __init__(self,largo,ancho):
        self.largo=largo
        self.ancho=ancho

    def calculo_techo(self):
        'Cantidad de chapas necesarias'
        y=self.largo*self.ancho
        chapa=float(input("""ingrese la medida de las chapas:\n """))
        cantidad=round(y/chapa,2)
        print("%s chapas"%(cantidad))
        cadena=[cantidad]
        return cadena

    def calculo_correas(self):
        'cantidad de tirantes o correas necesarias para el techo '
        maximo=max(self.largo,self.ancho)
        separacion=float(input("ingrese la separacion entre tirantes"))
        dato=round(maximo-separacion*2,2)
        total=round(dato/separacion,2)+2
        print("%s correas"%(total))
        cadena=[total]
        return cadena
#---------------------------------------------------------------
n=Techos(20,10)
n.calculo_correas()