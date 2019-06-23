
class Contrapiso_calculo():
    def __init__(self,largo,ancho,espesor):
        self.largo = largo
        self.ancho = ancho
        self.espesor = espesor
        self.detalle=[]
    def calcular_Contrapiso(self):
        m3= self.largo*self.ancho*self.espesor
        cemento= round(38.4*m3)
        arena = round(0.51*m3)
        cascote= round(0.77*m3)
        cemento_alba= round(105*m3)
        cascote2= round(0.90*m3)
        cal= round(81*m3)
        self.detalle.append(cemento)
        self.detalle.append(arena)
        self.detalle.append(cascote)
#----------------------------------------------------
x=Contrapiso_calculo(8,8,0.15)
x.calcular_Contrapiso()
print(x.detalle)