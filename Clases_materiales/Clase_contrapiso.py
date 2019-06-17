#clase calculo de contrapiso--------------------
class Contrapiso():
    def __init__(self,largo,ancho,espesor):
        self.largo = largo
        self.ancho = ancho
        self.espesor = espesor
    
    def calcular_Contrapiso(self):
        'Realiza el calculo del contrapiso'
        m3= self.largo*self.ancho*self.espesor
        cemento= round(38.4*m3,2)
        arena = round(0.51*m3,2)
        cascote= round(0.77*m3,2)
        cemento_alba= round(105*m3,2)
        cascote2= round(0.90*m3,2)
        cal= round(81*m3,2)
        print("{0}Kg Cemento ,{1}Kg Cal ,{2} M3 arena ,{3} M3 de Piedra".format(cemento,cal,arena,cascote))
        cadena =[cemento,cal,arena,cascote]
        return cadena
#-------------------------------------------------
c = Contrapiso(12,3,0.15)
c.calcular_Contrapiso()
