
class Contrapiso():
    def __init__(self,largo,ancho,espesor):
        self.largo = largo
        self.ancho = ancho
        self.espesor = espesor
    
    def calcular_Contrapiso(self):
        m3= self.largo*self.ancho*self.espesor
        cemento= round(38.4*m3)
        arena = round(0.51*m3)
        cascote= round(0.77*m3)
        cemento_alba= round(105*m3)
        cascote2= round(0.90*m3)
        cal= round(81*m3)
        print("Valor calculado: cemento= {0}, arena= {1}, cascote= {2}, cemento_alba= {3}, cascote2= {4},cal= {5}".format(cemento,arena,cascote,cemento_alba,cascote2,cal))
        cadena =[cemento,arena,cascote,cemento_alba,cascote2,cal]
        return cadena

c = Contrapiso(12,3,0.15)
c.calcular_Contrapiso()
