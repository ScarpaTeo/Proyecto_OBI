import sys
sys.path.append('../vista')
from calculoCimiento import Cimiento
from calculorRevoque import Revoque
from calculoContrapiso import Contrapiso
from calcularTecho import Techo
from calculoPared import Pared
class Controllercalculo():
    
    def verCimiento(self):
        ci=Cimiento()
        dato=ci.vistaCimiento()
        
        #vuelve atras
        if dato==True:
            #se tiene que levantar la clase principal
            print("cerrar ventana", dato)

        #trae los datos para calcular
        if dato!=False and dato!=True:
            #traer datos de la DB
            #realizar los calculos
            resultado=dato['alto']+dato['ancho']+dato['profundidad']
            ci.vistaCimiento(resultado)

    def verRevoque(self):
        ci=Revoque()
        dato=ci.vistaRevoque()
        
        #vuelve atras
        if dato==True:
            #se tiene que levantar la clase principal
            print("vuelve atras")
        #trae los datos para calcular
        if dato!=False and dato!=True:
            #traer datos de la DB
            #realizar los calculos
            resultado=dato['alto']+dato['ancho'] 
            ci.vistaRevoque(resultado)
    
    def verContrapiso(self):
        ci=Contrapiso()
        dato=ci.vistaContrapiso()
        
        #vuelve atras
        if dato==True:
            #se tiene que levantar la clase principal
            print("vuelve atras")
        #trae los datos para calcular
        if dato!=False and dato!=True:
            #traer datos de la DB
            #realizar los calculos
            resultado=dato['alto']+dato['ancho']+dato['profundidad'] 
            ci.vistaContrapiso(resultado)
    
    def verPared(self):
        ci=Pared()
        dato=ci.vistaPared()
        
        #vuelve atras
        if dato==True:
            #se tiene que levantar la clase principal
            print("vuelve atras")
        #trae los datos para calcular
        if dato!=False and dato!=True:
            #traer datos de la DB
            #realizar los calculos
            resultado=dato['alto']+dato['ancho']
            ci.vistaPared(resultado)
    
    def verTecho(self):
        ci=Techo()
        dato=ci.vistaTecho()
        
        #vuelve atras
        if dato==True:
            #se tiene que levantar la clase principal
            print("vuelve atras")
        #trae los datos para calcular
        if dato!=False and dato!=True:
            #traer datos de la DB
            #realizar los calculos
            resultado=dato['alto']+dato['ancho']
            ci.vistaTecho(resultado)