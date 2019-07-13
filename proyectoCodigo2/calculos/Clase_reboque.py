
class Reboque:
    def __init__(self,largo=1,alto=1):
        self.largo = largo
        self.alto = alto
        self.detalle=[]
    
    def reboqueImpermeable(self):
        lista1=[]
        espesor = 0.005
        m3 = self.largo*self.alto*espesor
        cemento_hidro = round(2.7*m3,2)
        arena_hidro =round(0.06*m3,3)
        lista1.append(cemento_hidro)
        lista1.append(0)
        lista1.append(arena_hidro)
        self.detalle.append(lista1)
        
    def reboqueGrueso(self):
        list2=[]
        espesor = 0.015
        m3 = self.largo*self.alto*espesor
        cemento_gru =round(1.85*m3,2)
        arena_gru =round(0.17*m3,3)
        cal_gru=round(3.6*m3,2)
        list2.append(cemento_gru)
        list2.append(cal_gru)
        list2.append(arena_gru)
        self.detalle.append(list2)

    def reboqueFino(self):
        lista3=[]
        espesor = 0.005
        m3 = self.largo*self.alto*espesor
        cemento_fi =round(0.45*m3,2)
        arena_fi =round(0.06*m3,3)
        cal_fi=round(1.6*m3,2)       
        lista3.append(cemento_fi)
        lista3.append(cal_fi)
        lista3.append(arena_fi)
        self.detalle.append(lista3)
    def reboqueExterior(self):
        self.reboqueImpermeable()
        self.reboqueGrueso()
        self.reboqueFino()
        a=0
        b=0
        c=0
        for item in self.detalle:
            for element in item:
                a+=float(item[0])
                b+=float(item[1])
                c+=float(item[2])
        lista=[a,b,c]
        self.detalle=lista

    def reboqueinterior(self):
        self.reboqueGrueso()
        self.reboqueFino()
        a=0
        b=0
        c=0
        for item in self.detalle:
            for element in item:
                a+=float(item[0])
                b+=float(item[1])
                c+=float(item[2])
        lista=[a,b,c]
        self.detalle=lista





#re=Reboque(4,10)
#re.reboqueExterior()
#print(re.detalle)
