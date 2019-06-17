#Clase calculo de revoques----------------------------------------
class Revoque:
    def __init__(self,largo=1,alto=1):
        self.largo = largo
        self.alto = alto
    
    def revoqueImpermeable(self):
        'Calculo de revoque impermeable de cemento'
        espesor = 0.005
        m3 = self.largo*self.alto*espesor
        cemento_hidro = round(2.7*m3,2)
        arena_hidro =round(0.06*m3,2)
        print("{0}Kg Cemento ,{1} M3 Arena".format(cemento_hidro,arena_hidro))
        cadena=[cemento_hidro,arena_hidro]
        return cadena
        
    def revoqueGrueso(self):
        'Calculo de revoque grueso de cal'
        espesor = 0.015
        m3 = self.largo*self.alto*espesor
        cemento_gru =round(1.85*m3,2)
        arena_gru =round(0.17*m3,2)
        cal_gru=round(3.6*m3,2)
        print("{0}Kg Cemento ,{1}kg Cal ,{2} M3 Arena".format(cemento_gru,cal_gru,arena_gru))
        cadena =[cemento_gru,cal_gru,arena_gru]
        return cadena

    def revoqueFino(self):
        'calculo de revoque fino de cal'
        espesor = 0.005
        m3 = self.largo*self.alto*espesor
        cemento_fi =round(0.45*m3,2)
        arena_fi =round(0.06*m3,2)
        cal_fi=round(1.6*m3,2)
        print("{0}Kg Cemento ,{1}kg Cal ,{2} M3 Arena".format(cemento_fi,cal_fi,arena_fi))
        cadena = [cemento_fi,cal_fi,arena_fi]
        return cadena
#--------------------------------------------------
re = Revoque(6,4)
re.revoqueImpermeable()
