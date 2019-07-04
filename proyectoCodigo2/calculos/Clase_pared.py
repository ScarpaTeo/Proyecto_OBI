
#-------------------------------------------------------------------1) clase de calculo paredes de Bloques
class Pared_Bloques:
    def __init__(self,largo=1,alto=1):
        self.largo=largo
        self.alto=alto
        self.detalle=[]
    def calculo_PC15(self):
        'Calculo pared de Bloques ceramico de 15cm'
        y = self.largo*self.alto
        cal = round(2.5 * y,2)
        cemento = round(0.65 * y,2)
        arena = round(0.12 * y ,2)
        bloques = round(12.5 * y,2)
        self.detalle.append(cal)
        self.detalle.append(cemento)
        self.detalle.append(arena)
        self.detalle.append(bloques)

    def calculo_PC20(self):
        'calculo pared de Bloques ceramicos de 20cm'
        y = self.largo * self.alto
        cal = round( 3 * y, 2)
        cemento = round(0.78 * y, 2)
        arena = round(0.15 * y, 2)
        bloques = round(12.5 * y, 2)
        self.detalle.append(cal)
        self.detalle.append(cemento)
        self.detalle.append(arena)
        self.detalle.append(bloques)
    def calculo_PH10(self):
        'calculo pared de Bloques de hormigon de 10cm'
        y = self.largo*self.alto
        cal = round(1.9 * y,2)
        cemento = round(1.95 * y,2)
        arena = round(0.13 * y ,2)
        bloques = round(12.5 * y,2)
        self.detalle.append(cal)
        self.detalle.append(cemento)
        self.detalle.append(arena)
        self.detalle.append(bloques)
    def calculo_PH20(self):
        'calculo pared de Bloques de hormigon de 20cm'
        y = self.largo*self.alto
        cal = round(1.5 * y,2)
        cemento = round(3.30 * y,2)
        arena = round(0.15 * y ,2)
        bloques = round(12.5 * y,2)
        self.detalle.append(cal)
        self.detalle.append(cemento)
        self.detalle.append(arena)
        self.detalle.append(bloques)
#-----------------------------------------------------------------------------2) clase de calculo paredes de Tabiques
class Pared_tabiques:
    def __init__(self,largo=1,alto=1):
        self.largo=largo
        self.alto=alto
        self.detalle=[]
    def calculo_PH15(self):
        'Calculo pared de tabique ceramico hueco de 15cm'
        y = self.largo*self.alto
        cal = round(3.4 * y,2)
        cemento = round(3.5 * y,2)
        arena = round(0.16 * y ,2)
        bloques = round(30 * y,2)
        self.detalle.append(cal)
        self.detalle.append(cemento)
        self.detalle.append(arena)
        self.detalle.append(bloques)
    def calculo_PH20(self):
        'Calculo pared de tabique ceramico hueco de 20cm'
        y = self.largo*self.alto
        cal = round(7.8 * y,2)
        cemento = round(8 * y,2)
        arena = round(0.37 * y ,2)
        bloques = round(33 * y,2)
        self.detalle.append(cal)
        self.detalle.append(cemento)
        self.detalle.append(arena)
        self.detalle.append(bloques)
#-------------------------------------------------------------------------3) clase pared de ladrillo común
class Pared_Comun:
    def __init__(self,largo=1,alto=1):
        self.largo=largo
        self.alto=alto
        self.detalle=[]
    def calculo_PC15(self):
        'Calculo pared de tabique ceramico hueco de 20cm'
        y = self.largo*self.alto
        cal = round(7.3 * y,2)
        cemento = round(7.5 * y,2)
        arena = round(0.35 * y ,2)
        bloques = round(60 * y,2)
        self.detalle.append(cal)
        self.detalle.append(cemento)
        self.detalle.append(arena)
        self.detalle.append(bloques)
    def calculo_PC20(self):
        'Calculo pared de tabique ceramico hueco de 20cm'
        y = self.largo*self.alto
        cal = round(13.20 * y,2)
        cemento = round(6.9 * y,2)
        arena = round(0.65 * y ,2)
        bloques = round(90 * y,2)
        self.detalle.append(cal)
        self.detalle.append(cemento)
        self.detalle.append(arena)
        self.detalle.append(bloques)
    def calculo_PC30(self):
        'Calculo pared de tabique ceramico hueco de 20cm'
        y = self.largo*self.alto
        cal = round(19.10 * y,2)
        cemento = round(9.90 * y,2)
        arena = round(0.90 * y ,2)
        bloques = round(120 * y,2)
        self.detalle.append(cal)
        self.detalle.append(cemento)
        self.detalle.append(arena)
        self.detalle.append(bloques)

#-----------------------------------------
#pared1=Pared_tabiques(10,4)
#a=pared1.calculo_PH15()
#print(a)

#pared2=Pared_Bloques(10,4)
#b=pared2.calculo_PC20()
#print(b)

#pared3=Pared_Comun(10,4)
#c=pared3.calculo_PC15()
#print(c)