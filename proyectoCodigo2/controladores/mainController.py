
import sys
sys.path.append('../vista')
sys.path.append('../modelos')
from loginModel import LoginModel
from Inicio import Login
from Principal import Principal
from calculoCimiento import Cimiento
from calculorRevoque import Revoque
from calculoContrapiso import Contrapiso
from calcularTecho import Techo
from calculoPared import Pared
from Menu import *
sys.path.append('../calculos')
from Clase_cimiento import *
from Clase_contrapiso import *
from Clase_reboque import *
from Clase_pared import *
from clase_Techos import *
from Error_Usuario import *

class Controlador():
    def __init__(self):
        self.detalleGeneral=[]

    def validarUsuario(self):
        modelo = LoginModel()
        lo = Login()
        datos = lo.Motrar()
        if not datos['user'] or not datos['pass']:
            self.erroCamVacios()
        else:
            validacion = modelo.validarUsuarioModel(datos['user'], datos['pass'])
            if (validacion == True):
                self.levantarMenu()
            else:
                self.errorUIncorrecto()

    def erroCamVacios(self):
        er = Error_Usuario()
        dato = er.errorCamposVacios()

        if dato == "cerrar":
            self.validarUsuario()

    def errorUIncorrecto(self):
        err = Error_Usuario()
        dato = err.errorUsarioIncorrecto()
        if dato == "cerrar":
            self.validarUsuario()

    def levantarMenu(self):
        m=MostrarMenu()
        m.mostrar()
        dato=m.valor
        if dato=="precios":
            pass
        elif dato=="presupuesto":
            self.levantarVentanaCalculo()

    def levantarVentanaCalculo(self):
        pri=Principal()
        tipo=pri.mostrar()
        if tipo=="cimiento":
            self.verCimiento()
        elif tipo=="revoque":
            self.verRevoque()
        elif tipo=="contrapiso":
            self.verContrapiso()
        elif tipo=="pared":
            self.verPared()
        elif tipo=="techo":
            self.verTecho()
        elif tipo=="menu":
            self.levantarMenu()

    def verTecho(self):
        t=Techo()
        t.vistaTecho()
        dato=t.valor
        if dato == True or dato == "principal":
            self.levantarVentanaCalculo()
        if dato != False and dato != True:
            nuevo = Techos_calculo(dato['alto'], dato['ancho'], dato['tipo'])
            nuevo.calculo_techo()
            lista1 = nuevo.detalle
            precios = [(1000)]
            total = [a * b for a, b in zip(precios, lista1)]
            string = '''
    Chapas...{0}\n
    Total...${1}'''.format(round(lista1[0], 2), round(sum(total), 2))
            new_t= t.vistaTecho(string, "disable")
            self.detalleGeneral.append(string)
            if t.valor == "principal":
                self.levantarVentanaCalculo()
    def verCimiento(self):
        c=Cimiento()
        c.vistaCimiento()
        dato=c.valor
        if dato == True or dato == "principal":
            self.levantarVentanaCalculo()
        if dato != False and dato != True:
            if dato['tipo_a_calcular']=='Corrida':
                nuevo = Zapata_corrida(dato['alto'], dato['ancho'], dato['profundidad'])
                nuevo.Corrida_cemento()
                lista1 = nuevo.detalle
            elif dato['tipo_a_calcular']=='viga':
                nuevo = Viga_encadenado(dato['alto'], dato['ancho'], dato['profundidad'])
                nuevo.calculo_Viga()
                lista1 = nuevo.detalle
            elif dato['tipo_a_calcular']=='pilotin':
                nuevo = Pilotines(dato['alto'], dato['ancho'], dato['profundidad'])
                nuevo.calculo_pilotin()
                lista1 = nuevo.detalle
            precios = [(7.8), (1450), (2100),(850),(550)]
            total = [a * b for a, b in zip(precios, lista1)]
            string = '''
    Cemento...{0} kg\n
    Arena...{1} m3\n
    Piedra...{2} m3\n
    Hierro 10...{3}m\n
    Hierro 4...{4}m\n
    Total...${5}'''.format(round(lista1[0], 2), round(lista1[1], 2), round(lista1[2], 2), round(lista1[3], 2), round(lista1[4], 2),round(sum(total), 2))
            new_c = c.vistaCimiento(string, "DISABLE")
            self.detalleGeneral.append(string)
            if c.valor == "principal":
                self.levantarVentanaCalculo()

    def verRevoque(self):
        r=Revoque()
        r.vistaRevoque()
        dato=r.valor
        if dato == True or dato == "principal":
            self.levantarVentanaCalculo()
        if dato != False and dato != True:
            if dato["tipo"]=="Reboque Grueso":
                nuevo = Reboque(dato['alto'], dato['ancho'])
                nuevo.reboqueGrueso()
                lista1 = nuevo.detalle
            elif dato["tipo"]=="Revoque Impearmeable":
                nuevo = Reboque(dato['alto'], dato['ancho'])
                nuevo.reboqueImpermeable()
                lista1 = nuevo.detalle
            elif dato["tipo"]=="Reboque fino":
                nuevo = Reboque(dato['alto'], dato['ancho'])
                nuevo.reboqueFino()
                lista1 = nuevo.detalle
            precios = [(10), (7.8), (1450)]
            total = [a * b for a, b in zip(precios, lista1)]
            string = '''
    Cal...{0} kg\n
    Cemento...{1} kg\n
    Arena...{2} m3\n
    Total...${3}'''.format(round(lista1[0], 2), round(lista1[1], 2), round(lista1[2], 2),round(sum(total), 2))
            new_r = r.vistaRevoque(string, "disable")
            self.detalleGeneral.append(string)
            if r.valor == "principal":
                self.levantarVentanaCalculo()

    def verContrapiso(self):
        cn=Contrapiso()
        cn.vistaContrapiso()
        dato=cn.valor
        if dato == True or dato == "principal":
            self.levantarVentanaCalculo()
        if dato != False and dato != True:
            nuevo = Contrapiso_calculo(dato['alto'], dato['ancho'], dato['profundidad'])
            nuevo.calcular_Contrapiso()
            lista1 = nuevo.detalle
            precios = [(7.8), (1450), (1100)]
            total = [a * b for a, b in zip(precios, lista1)]
            string = '''
    Cemento...{0} kg\n
    Arena...{1} m3\n
    Piedra...{2} m3\n
    Total...${3}'''.format(round(lista1[0], 2), round(lista1[1], 2), round(lista1[2], 2),round(sum(total), 2))
            new_cn = cn.vistaContrapiso(string, "disable")
            self.detalleGeneral.append(string)
            if cn.valor == "principal":
                self.levantarVentanaCalculo()

    def verPared(self):
        p=Pared()
        p.vistaPared()
        dato=p.valor
        if dato == True or dato == "principal":
            self.levantarVentanaCalculo()
        if dato != False and dato != True:
            if dato['tipo']=='Pared de Bloques' and dato['espesor']=='0.15 cm':
                nuevo = Pared_Bloques(dato['alto'], dato['ancho'])
                nuevo.calculo_PC15()
                lista1 = nuevo.detalle
            elif dato['tipo']=='Pared de Bloques' and dato['espesor']=='0.20 cm':
                nuevo = Pared_Bloques(dato['alto'], dato['ancho'])
                nuevo.calculo_PC20()
                lista1 = nuevo.detalle
            elif dato['tipo']=='Pared de Bloques' and dato['espesor']=='0.30 cm':
                nuevo = Pared_Bloques(dato['alto'], dato['ancho'])
                nuevo.calculo_PC20()
                lista1 = nuevo.detalle
            elif dato['tipo']=='Pared de Tabiques' and dato['espesor']=='0.15 cm':
                nuevo = Pared_tabiques(dato['alto'], dato['ancho'])
                nuevo.calculo_PH15()
                lista1 = nuevo.detalle
            elif dato['tipo']=='Pared de Tabiques' and dato['espesor']=='0.20 cm':
                nuevo = Pared_tabiques(dato['alto'], dato['ancho'])
                nuevo.calculo_PH20()
                lista1 = nuevo.detalle
            elif dato['tipo']=='Pared de Tabiques' and dato['espesor']=='0.30 cm':
                nuevo = Pared_tabiques(dato['alto'], dato['ancho'])
                nuevo.calculo_PH20()
                lista1 = nuevo.detalle
            elif dato['tipo']=='Pared Común' and dato['espesor']=='0.15 cm':
                nuevo = Pared_Comun(dato['alto'], dato['ancho'])
                nuevo.calculo_PC15()
                lista1 = nuevo.detalle
            elif dato['tipo']=='Pared Común' and dato['espesor']=='0.20 cm':
                nuevo = Pared_Comun(dato['alto'], dato['ancho'])
                nuevo.calculo_PC20()
                lista1 = nuevo.detalle
            elif dato['tipo'] == 'Pared Común' and dato['espesor'] == '0.30 cm':
                nuevo = Pared_Comun(dato['alto'], dato['ancho'])
                nuevo.calculo_PC30()
                lista1 = nuevo.detalle

            precios = [(10), (7.8), (1450), (4)]
            total = [a * b for a, b in zip(precios, lista1)]
            string = '''
        Cal...${0} kg\n
        Cemento...${1} kg\n
        Arena...{2} m3\n
        Ladrillos...{3}
        Total...${4}'''.format(round(lista1[0], 2), round(lista1[1], 2), round(lista1[2], 2),round(lista1[3], 2),round(sum(total), 2))
            new_p = p.vistaPared(string, "disable")
            self.detalleGeneral.append(string)
            if p.valor == "principal":
                self.levantarVentanaCalculo()

if __name__=="__main__":
    new=Controlador()
    new.validarUsuario()
    print(new.detalleGeneral)