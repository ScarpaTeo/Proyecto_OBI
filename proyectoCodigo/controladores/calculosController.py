import sys
sys.path.append('../vista')
from calculoCimiento import Cimiento
from calculorRevoque import Revoque
from calculoContrapiso import Contrapiso
from calcularTecho import Techo
from calculoPared import Pared
sys.path.append('../calculos')
from Clase_cimiento import *
from Clase_contrapiso import *
from Clase_reboque import *
from Clase_pared import *
from clase_Techos import *
import PrincipalController
import ErrorCalculosController

class Controllercalculo():
    
    def verCimiento(self):
        def calcular(dato):
            if dato=="principal":
                x=PrincipalController.ControllerPrincipal()
                x.levantarVentanaCalculo()
            #trae los datos para calcular
            if dato!=False and dato!=True:
                #traer datos de la DB
                #realizar los calculo
                nuevo=Zapata_corrida(dato['alto'],dato['ancho'],dato['profundidad'])
                nuevo.Corrida_cemento()
                lista1=nuevo.detalle
                precios = [(10), (7.8), (1450), (2100)]
                total = [a * b for a, b in zip(precios, lista1)]
                string = '''
                Cal...${0}\n
                Cemento...${1}\n
                Arena...${2}\n
                Piedra...${3}\n
                Total...${4}'''.format(round(total[0],2),round(total[1],2),round(total[2],2),round(total[3],2), round(sum(total),2))
                dato=ci.vistaCimiento(string,"DISABLE")
                calcular(dato)
        ci=Cimiento()
        dato=ci.vistaCimiento()
        calcular(dato)
        
    def verRevoque(self):
        ci=Revoque()
        dato=ci.vistaRevoque()
        
        #vuelve atras
        if dato==True:
            x=PrincipalController.ControllerPrincipal()
            x.levantarVentanaCalculo()

        #trae los datos para calcular
        if dato!=False and dato!=True:
            #traer datos de la DB
            #realizar los calculos
            nuevo = Reboque(dato['alto'], dato['ancho'])
            nuevo.reboqueGrueso()
            lista1 = nuevo.detalle
            precios = [(10), (7.8), (1450)]
            total = [a * b for a, b in zip(precios, lista1)]
            string = '''
            Cal...${0}\n
            Cemento...${1}\n
            Arena...${2}\n
            Total...${3}'''.format(round(total[0], 2), round(total[1], 2), round(total[2], 2),round(sum(total), 2))
            ci.vistaRevoque(string)
    
    def verContrapiso(self):
        ci=Contrapiso()
        dato=ci.vistaContrapiso()
        
        #vuelve atras
        if dato==True:
            x=PrincipalController.ControllerPrincipal()
            x.levantarVentanaCalculo()

        #trae los datos para calcular
        if dato!=False and dato!=True:
            #traer datos de la DB
            #realizar los calculos
            nuevo=Contrapiso_calculo(dato['alto'],dato['ancho'],dato['profundidad'])
            nuevo.calcular_Contrapiso()
            lista1=nuevo.detalle
            precios = [(7.8), (1450), (1100)]
            total = [a * b for a, b in zip(precios, lista1)]
            string = '''
            Cemento...${0}\n
            Arena...${1}\n
            Piedra...${2}\n
            Total...${3}'''.format(round(total[0],2),round(total[1],2),round(total[2],2),round(sum(total),2))
            ci.vistaContrapiso(string)
    
    def verPared(self):
        ci=Pared()
        dato=ci.vistaPared()
        
        #vuelve atras
        if dato==True:
            x=PrincipalController.ControllerPrincipal()
            x.levantarVentanaCalculo()

        #trae los datos para calcular
        if dato!=False and dato!=True:
            #traer datos de la DB
            #realizar los calculos
            nuevo = Pared_Comun(dato['alto'], dato['ancho'])
            nuevo.calculo_PC15()
            lista1 = nuevo.detalle
            precios = [(10), (7.8), (1450),(4)]
            total = [a * b for a, b in zip(precios, lista1)]
            string = '''
            Cal...${0}\n
            Cemento...${1}\n
            Arena...${2}\n
            Ladrillos...${3}
            Total...${4}'''.format(round(total[0], 2), round(total[1], 2), round(total[2], 2), round(total[3], 2),round(sum(total), 2))
            ci.vistaPared(string)
    
    def verTecho(self):
        ci=Techo()
        dato=ci.vistaTecho()
        
        #vuelve atras
        if dato==True:
            x=PrincipalController.ControllerPrincipal()
            x.levantarVentanaCalculo()

        #trae los datos para calcular
        if dato!=False and dato!=True:
            #traer datos de la DB
            #realizar los calculos
            nuevo = Techos_calculo(dato['alto'], dato['ancho'],dato['tipo'])
            nuevo.calculo_techo()
            lista1 = nuevo.detalle
            precios = [(1000)]
            total = [a * b for a, b in zip(precios, lista1)]
            string = '''
            Chapas...{0}\n
            Total...${1}'''.format(round(lista1[0], 2),round(sum(total), 2))
            ci.vistaTecho(string)