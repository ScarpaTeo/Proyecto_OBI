
class Reboque:
    def __init__(self,largo=1,alto=1):
        self.largo = largo
        self.alto = alto
        self.detalle=[]
    
    def reboqueImpermeable(self):
        espesor = 0.005
        m3 = self.largo*self.alto*espesor
        cemento_hidro = round(2.7*m3,2)
        arena_hidro =round(0.06*m3,2)
        self.detalle.append(cemento_hidro)
        self.detalle.append(arena_hidro)
        
    def reboqueGrueso(self):
        espesor = 0.015
        m3 = self.largo*self.alto*espesor
        cemento_gru =round(1.85*m3)
        arena_gru =round(0.17*m3)
        cal_gru=round(3.6*m3)
        self.detalle.append(cemento_gru)
        self.detalle.append(cal_gru)
        self.detalle.append(arena_gru)

    def reboqueFino(self):
        espesor = 0.005
        m3 = self.largo*self.alto*espesor
        cemento_fi =round(0.45*m3)
        arena_fi =round(0.06*m3)
        cal_fi=round(1.6*m3)       
        self.detalle.append(cemento_fi)
        self.detalle.append(cal_fi)
        self.detalle.append(arena_fi)

#re = Reboque(24,43)
#re.reboqueFino()
