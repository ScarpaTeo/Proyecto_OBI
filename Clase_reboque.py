
class Reboque:
    def __init__(self,largo=1,alto=1):
        self.largo = largo
        self.alto = alto
    
    def reboqueImpermeable(self):
        espesor = 0.005
        m3 = self.largo*self.alto*espesor
        cemento_hidro = round(2.7*m3,2)
        arena_hidro =round(0.06*m3,2)
        print("Operacion calculado")
        cadena = "El valor calculado de cemento es:{c} y de arena es{a}".format(c=cemento_hidro,a=arena_hidro)
        return cadena
        
    def reboqueGrueso(self):
        espesor = 0.015
        m3 = self.largo*self.alto*espesor
        cemento_gru =round(1.85*m3)
        arena_gru =round(0.17*m3)
        cal_gru=round(3.6*m3)
        print("Valor de cemento es: {0}. Valor de arena es: {1}. Valor de cal es:{2}".format(cemento_gru,arena_gru,cal_gru))
        cadena =[cemento_gru,arena_gru,cal_gru]
        return cadena

    def reboqueFino(self):
        espesor = 0.005
        m3 = self.largo*self.alto*espesor
        cemento_fi =round(0.45*m3)
        arena_fi =round(0.06*m3)
        cal_fi=round(1.6*m3)       
        print("Valor de cemento es:{0}. Valor de arena es:{1}. Valor de cal es:{2}".format(cemento_fi,arena_fi,cal_fi))
        cadena = [cemento_fi,arena_fi,cal_fi]
        return cadena

re = Reboque(24,43)
re.reboqueFino()
