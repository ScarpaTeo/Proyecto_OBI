
#--------------------------------------------------------------------------------1)Clase calculo de zapata corrida
class Zapata_corrida:
    def __init__(self,largo=1,ancho=1,profundidad=1):
        self.largo=largo
        self.ancho=ancho
        self.profundidad=profundidad
    def Corrida_cemento(self):
        'Calculo de zapata corrida hecha con hormigon'
        y=self.largo*self.ancho*self.profundidad
        cal = round(81 * y,2)
        cemento = round(38.40 * y,2)
        arena = round(0.51 * y,2)
        cascote = round(0.77 * y,2)
        cadena="{0}Kg cal ,{1}Kg cementos ,{2}M3 arena ,{3}M3 piedra".format(cal,cemento,arena,cascote)
        print("objeto calculado")
        return cadena
    def Corrida_hercal(self):
        "Calculo de zapata corrida hecha con Hercal"
        y=self.largo*self.ancho*self.profundidad
        hercal = round(105 * y,2)
        arena = round(0.45 * y,2)
        cascote = round(0.9 * y,2)
        cadena="{0}Kg Hercal ,{1}M3 arena ,{3}M3 cascote".format(hercal,arena,cascote)
        print("objeto calculado")
        return cadena
#-------------------------------------------------------------------------2)clase calculo de Viga de encadenado
class Viga_encadenado:
    def __init__(self,largo=1,ancho=1,profundidad=1):
        self.largo=largo
        self.ancho=ancho
        self.profundidad=profundidad
    def calculo_Viga(self):
        'Calculo de viga de encadenado o de cintura'
        y=self.largo*self.ancho*self.profundidad
        cemento = round(12 * y,2)
        arena = round(0.26 * y,2)
        piedra = round(0.26 * y,2)
        hierro10 = round(4 * y,2)
        hierro4 = round(3.50 * y,2)
        cadena="{0}Kg cemento ,{1}M3 arena ,{2}M3 piedra ,{3}m Hierros del 10 ,{4}m Hierros del 4".format(cal,cemento,arena,piedra,hierro10,hierro4)
        print("objeto calculado")
        return cadena
#----------------------------------------------------------------------3)clase calculo de Pilotines
class Pilotines:
    def __init__(self,diametro=0.2,profundidad=1,cantidad=1):
        self.diametro=diametro
        self.profundidad=profundidad
        self.cantidad=cantidad
    def calculo_pilotin(self):
        'Calculo de Pilotines de Hormigon'
        from math import pi
        y= pi*(self.diametro/2)*self.profundidad
        x= self.cantidad
        cemento = round(14.70*y*x,2)
        arena = round(0.32*y*x,2)
        piedra = round(0.32*y*x,2)
        hierro10= round(5.5*y*x,2)
        hierro4= round(3.50*y*x,2)
        cadena="{0}Kg cemento ,{1}M3 arena ,{2}M3 piedra ,{3}m Hierros del 10 ,{4}m Hierros del 4".format(cal,cemento,arena,piedra,hierro10,hierro4)
        print("objeto calculado")
        return cadena

#---------------------------------------------------------------------------4)