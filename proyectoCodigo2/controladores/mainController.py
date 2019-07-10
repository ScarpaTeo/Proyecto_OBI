
import sys
sys.path.append('../conexion')
from Clase_ConsultaBD import Conexion
from Reporte import generaReporte
sys.path.append('../vista')
sys.path.append('../modelos')
from loginModel import LoginModel
from registroModel import RegitroModel
from actualizarPrecioModel import actualizarLosPrecioModel
from ventanaRegistro import Registro
from Inicio import Login
from Principal import Principal
from calculoCimiento import Cimiento
from calculorRevoque import Revoque
from calculoContrapiso import Contrapiso
from calcularTecho import Techo
from calculoPared import Pared
from actualizarPrecio import ActualizarPrecio
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
        self.totales={
            "fecha":"09/06/19",
            "cimiento":"",
            "contrapiso":"",
            "revoque":"",
            "pared":"",
            "techo":""
        }

    def validarUsuario(self):
        modelo = LoginModel()
        lo = Login()
        datos = lo.Motrar()
        if datos == "Registro":
            self.levantarVentanaRegistro()

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
            self.levantarVentanaPrecio()
        elif dato=="presupuesto":
            self.levantarVentanaCalculo()
        elif dato=="cerrar Sesion":
            self.validarUsuario()

    def levantarVentanaRegistro(self):
        def registroo(datos):
            if datos=="Login":
                self.validarUsuario() 
            else:  
                registro=RegitroModel()
                bandera=registro.registrar(datos)
                reg=Registro()
                datos=reg.mostrarRegistro(bandera)
                registroo(datos)
        reg=Registro()
        datos=reg.mostrarRegistro()
        registroo(datos)

    def levantarVentanaPrecio(self):
        def levPrecio(dato):
            if dato == "principal":
                self.levantarMenu()
            else:
                actualizar = actualizarLosPrecioModel()
                cadena=actualizar.actualizarPrecioMateriales(dato['tipo'], dato['precio'])
                traer=actualizar.obtenerPrecios()
                detalle = ""
                for item in actualizar.dato:
                    texto = "%s.....$%s\n" % (str(item[1]), str(item[2]))
                    detalle += texto
                precioActualizado = ap.vistaActualizar(cadena,"disable",detalle)
                levPrecio(precioActualizado)

        ab=actualizarLosPrecioModel()
        ab.obtenerPrecios()
        print(ab.dato)
        detalle=""
        for item in ab.dato:
            texto="%s.....$%s\n"%(str(item[1]),str(item[2]))
            detalle+=texto

        ap = ActualizarPrecio()
        ap.vistaActualizar("","normal",str(detalle))
        dato= ap.valor
        levPrecio(dato)


    def levantarVentanaCalculo(self):
        pri=Principal()
        tipo=pri.mostrar()
        if tipo=="reporte":
            generaReporte(self.totales,"Presupuesto")
        elif tipo=="cimiento":
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
            descripcion = """
------------------OBI------------------\n
Cubierta de Chapa.\n
%s de Largo.\n
%s de Ancho.\n
Chapas de 1x%s.\n
------------------------------------------\n""" % (dato['alto'], dato['ancho'], dato['tipo'])
            descripcionh = """
------------------OBI------------------\n<br>
Cubierta de Chapa.\n<br>
%s de Largo.\n<br>
%s de Ancho.\n<br>
Chapas de 1x%s.\n<br>
------------------------------------------\n<br>""" % (dato['alto'], dato['ancho'], dato['tipo'])

            lista1 = nuevo.detalle
            precios = [(1000)]
            total = [a * b for a, b in zip(precios, lista1)]
            string = '''
    Chapas...{0}\n
    Total...${1}'''.format(round(lista1[0], 2), round(sum(total), 2))
            stringh = '''
    Chapas...{0}\n<br>
    Total...${1}'''.format(round(lista1[0], 2), round(sum(total), 2))
            
            texto = descripcion + string
            textohtm=descripcionh + stringh
            new_t= t.vistaTecho(texto, "disable")
            if t.valor=="principal":
                self.levantarVentanaCalculo()
            if t.valor == "añadir":
                self.totales['techo']=textohtm
                self.levantarVentanaCalculo()
    def verCimiento(self):
        c=Cimiento()
        c.vistaCimiento()
        dato=c.valor
        if dato == True or dato == "principal":
            self.levantarVentanaCalculo()
        if dato != False and dato != True:
            if dato['tipo_a_calcular']=='Zapata Corrida':
                nuevo = Zapata_corrida(dato['alto'], dato['ancho'], dato['profundidad'])
                nuevo.Corrida_cemento()
                descripcion = """
------------------OBI------------------\n
Zapata Corrida de H°.\n
%s de Largo.\n
%s de Ancho.\n
%s de Profundidad.\n
------------------------------------------\n""" % (dato['alto'], dato['ancho'], dato['profundidad'])
                descripcionh = """
------------------OBI------------------\n<br>
Zapata Corrida de H°.\n<br>
%s de Largo.\n<br>
%s de Ancho.\n<br>
%s de Profundidad.\n<br>
------------------------------------------\n<br>""" % (dato['alto'], dato['ancho'], dato['profundidad'])

                lista1 = nuevo.detalle
            elif dato['tipo_a_calcular']=='Viga de Hormigón':
                nuevo = Viga_encadenado(dato['alto'], dato['ancho'], dato['profundidad'])
                nuevo.calculo_Viga()
                descripcion = """
------------------OBI------------------\n
Viga de Encadenado H°.\n
%s de Largo.\n
%s de Ancho.\n
%s de Profundidad.\n
------------------------------------------\n""" % (dato['alto'], dato['ancho'], dato['profundidad'])
                descripcionh = """
------------------OBI------------------\n<br>
Viga de Encadenado H°.\n<br>
%s de Largo.\n<br>
%s de Ancho.\n<br>
%s de Profundidad.\n<br>
------------------------------------------\n<br>""" % (dato['alto'], dato['ancho'], dato['profundidad'])

                lista1 = nuevo.detalle
            elif dato['tipo_a_calcular']=='Pilotin de Hormigón':
                nuevo = Pilotines(dato['ancho'], dato['profundidad'],dato['alto'])
                nuevo.calculo_pilotin()
                descripcion="""
------------------OBI------------------\n
%s Pilotin de H°.\n
%s de Diametro.\n
%s de Profundidad.\n
------------------------------------------\n"""%(dato['alto'],dato['ancho'], dato['profundidad'])
                descripcionh="""
------------------OBI------------------\n<br>
%s Pilotin de H°.\n<br>
%s de Diametro.\n<br>
%s de Profundidad.\n<br>
------------------------------------------\n<br>"""%(dato['alto'],dato['ancho'], dato['profundidad'])

                lista1 = nuevo.detalle

            query = "SELECT precio FROM materiales WHERE id_materiales=2 or id_materiales=3 or id_materiales=4 or id_materiales=5 or id_materiales=6"
            traer = Conexion()
            precios2 = traer.ejecutar_get(query)
            precios = []
            for item in precios2:
                for element in item:
                    precios.append(int(element))

            #precios = [(7.8), (1450), (2100),(850),(550)]
            total = [a * b for a, b in zip(precios, lista1)]
            string = '''
Cemento...{0} kg\n
Arena...{1} m3\n
Piedra...{2} m3\n
Hierro 10...{3}m\n
Hierro 4...{4}m\n
------------------------------------------\n
Total...${5}'''.format(round(lista1[0], 2), round(lista1[1], 2), round(lista1[2], 2), round(lista1[3], 2), round(lista1[4], 2),round(sum(total), 2))
            stringh = '''
Cemento...{0} kg\n<br>
Arena...{1} m3\n<br>
Piedra...{2} m3\n<br>
Hierro 10...{3}m\n<br>
Hierro 4...{4}m\n<br>
------------------------------------------\n<br>
Total...${5}<br>'''.format(round(lista1[0], 2), round(lista1[1], 2), round(lista1[2], 2), round(lista1[3], 2), round(lista1[4], 2),round(sum(total), 2))

            texto=descripcion+string
            textohtm=descripcionh + stringh
            new_c = c.vistaCimiento(texto, "DISABLE")
            if c.valor=="principal":
                self.levantarVentanaCalculo()
            elif c.valor == "añadir":
                self.totales['cimiento']=textohtm
                self.levantarVentanaCalculo()

    def verRevoque(self):
        r=Revoque()
        r.vistaRevoque()
        dato=r.valor
        if dato == True or dato == "principal":
            self.levantarVentanaCalculo()
        if dato != False and dato != True:
            if dato["tipo"]=="Revoque Exterior Completo":
                nuevo = Reboque(dato['alto'], dato['ancho'])
                nuevo.reboqueExterior()
                descripcion = """
------------------OBI------------------\n
Revoque de Pared Exterior completo.\n
%s de Alto.\n
%s de Ancho.\n
------------------------------------------\n""" % (dato['alto'], dato['ancho'])
                descripcionh = """
------------------OBI------------------\n<br>
Revoque de Pared Exterior completo.\n<br>
%s de Alto.\n<br>
%s de Ancho.\n<br>
------------------------------------------\n<br>""" % (dato['alto'], dato['ancho'])

                lista1 = nuevo.detalle
            elif dato["tipo"]=="Revoque Interior Completo":
                nuevo = Reboque(dato['alto'], dato['ancho'])
                nuevo.reboqueinterior()
                descripcion = """
------------------OBI------------------\n
Revoque de Pared Interior completo.\n
%s de Alto.\n
%s de Ancho.\n
------------------------------------------\n""" % (dato['alto'], dato['ancho'])
                descripcionh = """
------------------OBI------------------\n<br>
Revoque de Pared Interior completo.\n<br>
%s de Alto.\n<br>
%s de Ancho.\n<br>
------------------------------------------\n<br>""" % (dato['alto'], dato['ancho'])

                lista1 = nuevo.detalle


            query = "SELECT precio FROM materiales WHERE id_materiales=1 or id_materiales=2 or id_materiales=3"
            traer = Conexion()
            precios2 = traer.ejecutar_get(query)
            precios = []
            for item in precios2:
                for element in item:
                    precios.append(int(element))

            #precios = [(10), (7.8), (1450)]
            total = [a * b for a, b in zip(precios, lista1)]
            string = '''
Cal...{0} kg\n
Cemento...{1} kg\n
Arena...{2} m3\n
------------------------------------------\n
Total...${3}'''.format(round(lista1[0], 2), round(lista1[1], 2), round(lista1[2], 3),round(sum(total), 2))
            stringh = '''
Cal...{0} kg\n<br>
Cemento...{1} kg\n<br>
Arena...{2} m3\n<br>
------------------------------------------\n<br>
Total...${3}<br>'''.format(round(lista1[0], 2), round(lista1[1], 2), round(lista1[2], 3),round(sum(total), 2))

            texto = descripcion + string
            textohtm=descripcionh + stringh
            new_r = r.vistaRevoque(texto, "disable")
            if r.valor=="principal":
                 self.levantarVentanaCalculo()
            if r.valor == "añadir":
                self.totales['revoque']=textohtm
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
            descripcion = """
------------------OBI------------------\n
Contrapiso de H°.\n
%s de Largo.\n
%s de Ancho.\n
%s de Espesor.\n
------------------------------------------\n""" % (dato['alto'], dato['ancho'],dato['profundidad'])
            descripcionh = """
------------------OBI------------------\n<br>
Contrapiso de H°.\n<br>
%s de Largo.\n<br>
%s de Ancho.\n<br>
%s de Espesor.\n<br>
------------------------------------------\n<br>""" % (dato['alto'], dato['ancho'],dato['profundidad'])

            lista1 = nuevo.detalle
            query = "SELECT precio FROM materiales WHERE id_materiales=2 or id_materiales=3 or id_materiales=4"
            traer = Conexion()
            precios2 = traer.ejecutar_get(query)
            precios = []
            for item in precios2:
                for element in item:
                    precios.append(int(element))

            #precios = [(7.8), (1450), (1100)]
            total = [a * b for a, b in zip(precios, lista1)]
            string = '''
Cemento...{0} kg\n
Arena...{1} m3\n
Piedra...{2} m3\n
------------------------------------------\n
Total...${3}'''.format(round(lista1[0], 2), round(lista1[1], 2), round(lista1[2], 2),round(sum(total), 2))
            stringh = '''
Cemento...{0} kg\n<br>
Arena...{1} m3\n<br>
Piedra...{2} m3\n<br>
------------------------------------------\n<br>
Total...${3}<br>'''.format(round(lista1[0], 2), round(lista1[1], 2), round(lista1[2], 2),round(sum(total), 2))

            texto = descripcion + string
            textohtm=descripcionh + stringh
            new_cn = cn.vistaContrapiso(texto, "disable")
            if cn.valor=="principal":
                self.levantarVentanaCalculo()
            if cn.valor == "añadir":
                self.totales['contrapiso']=textohtm
                self.levantarVentanaCalculo()

    def verPared(self):
        p=Pared()
        p.vistaPared()
        dato=p.valor
        if dato == True or dato == "principal":
            self.levantarVentanaCalculo()
        if dato != False and dato != True:
            if dato['tipo']=='Bloque Cerámico' and dato['espesor']=='0.15 cm':
                nuevo = Pared_Bloques(dato['alto'], dato['ancho'])
                nuevo.calculo_PC15()
                descripcion = """
------------------OBI------------------\n
Pared de Bloque Cerámico\n
%s de Alto.\n
%s de Ancho.\n
%s de Espesor.\n
------------------------------------------\n""" % (dato['alto'], dato['ancho'],dato['espesor'])
                descripcionh = """
------------------OBI------------------\n<br>
Pared de Bloque Cerámico\n<br>
%s de Alto.\n<br>
%s de Ancho.\n<br>
%s de Espesor.\n<br>
------------------------------------------\n<br>""" % (dato['alto'], dato['ancho'],dato['espesor'])

                lista1 = nuevo.detalle
                query = "SELECT precio FROM materiales WHERE id_materiales=1 or id_materiales=2 or id_materiales=3 or id_materiales=8"
            elif dato['tipo']=='Bloque Cerámico' and dato['espesor']=='0.20 cm':
                nuevo = Pared_Bloques(dato['alto'], dato['ancho'])
                nuevo.calculo_PC20()
                descripcion = """
------------------OBI------------------\n
Pared de Bloque Cerámico\n
%s de Alto.\n
%s de Ancho.\n
%s de Espesor.\n
------------------------------------------\n""" % (dato['alto'], dato['ancho'], dato['espesor'])
                descripcionh = """
------------------OBI------------------\n<br>
Pared de Bloque Cerámico\n<br>
%s de Alto.\n<br>
%s de Ancho.\n<br>
%s de Espesor.\n<br>
------------------------------------------\n<br>""" % (dato['alto'], dato['ancho'], dato['espesor'])

                lista1 = nuevo.detalle
                query = "SELECT precio FROM materiales WHERE id_materiales=1 or id_materiales=2 or id_materiales=3 or id_materiales=9"
            elif dato['tipo']=='Bloque Cerámico' and dato['espesor']=='0.30 cm':
                nuevo = Pared_Bloques(dato['alto'], dato['ancho'])
                nuevo.calculo_PC20()
                descripcion = """
------------------OBI------------------\n
Pared de Bloque Cerámico\n
%s de Alto.\n
%s de Ancho.\n
%s de Espesor.\n
------------------------------------------\n""" % (dato['alto'], dato['ancho'], dato['espesor'])
                descripcionh = """
------------------OBI------------------\n<br>
Pared de Bloque Cerámico\n<br>
%s de Alto.\n<br>
%s de Ancho.\n<br>
%s de Espesor.\n<br>
------------------------------------------\n<br>""" % (dato['alto'], dato['ancho'], dato['espesor'])

                lista1 = nuevo.detalle
                query = "SELECT precio FROM materiales WHERE id_materiales=1 or id_materiales=2 or id_materiales=3 or id_materiales=9"
            elif dato['tipo']=='Bloque de Hormigón' and dato['espesor']=='0.15 cm':
                nuevo = Pared_tabiques(dato['alto'], dato['ancho'])
                nuevo.calculo_PH15()
                descripcion = """
------------------OBI------------------\n
Pared de Bloque Hormigón\n
%s de Alto.\n
%s de Ancho.\n
%s de Espesor.\n
------------------------------------------\n""" % (dato['alto'], dato['ancho'], dato['espesor'])
                descripcionh = """
------------------OBI------------------\n<br>
Pared de Bloque Hormigón\n<br>
%s de Alto.\n<br>
%s de Ancho.\n<br>
%s de Espesor.\n<br>
------------------------------------------\n<br>""" % (dato['alto'], dato['ancho'], dato['espesor'])

                lista1 = nuevo.detalle
                query = "SELECT precio FROM materiales WHERE id_materiales=1 or id_materiales=2 or id_materiales=3 or id_materiales=10"
            elif dato['tipo']=='Bloque de Hormigón' and dato['espesor']=='0.20 cm':
                nuevo = Pared_tabiques(dato['alto'], dato['ancho'])
                nuevo.calculo_PH20()
                descripcion = """
------------------OBI------------------\n
Pared de Bloque Hormigón\n
%s de Alto.\n
%s de Ancho.\n
%s de Espesor.\n
------------------------------------------\n""" % (dato['alto'], dato['ancho'], dato['espesor'])
                descripcionh = """
------------------OBI------------------\n<br>
Pared de Bloque Hormigón\n<br>
%s de Alto.\n<br>
%s de Ancho.\n<br>
%s de Espesor.\n<br>
------------------------------------------\n<br>""" % (dato['alto'], dato['ancho'], dato['espesor'])

                lista1 = nuevo.detalle
                query = "SELECT precio FROM materiales WHERE id_materiales=1 or id_materiales=2 or id_materiales=3 or id_materiales=11"
            elif dato['tipo']=='Bloque de Hormigón' and dato['espesor']=='0.30 cm':
                nuevo = Pared_tabiques(dato['alto'], dato['ancho'])
                nuevo.calculo_PH20()
                descripcion = """
------------------OBI------------------\n
Pared de Bloque Hormigón\n
%s de Alto.\n
%s de Ancho.\n
%s de Espesor.\n
------------------------------------------\n""" % (dato['alto'], dato['ancho'], dato['espesor'])
                descripcionh = """
------------------OBI------------------\n<br>
Pared de Bloque Hormigón\n<br>
%s de Alto.\n<br>
%s de Ancho.\n<br>
%s de Espesor.\n<br>
------------------------------------------\n<br>""" % (dato['alto'], dato['ancho'], dato['espesor'])

                lista1 = nuevo.detalle
                query = "SELECT precio FROM materiales WHERE id_materiales=1 or id_materiales=2 or id_materiales=3 or id_materiales=11"
            elif dato['tipo']=='Ladrillo Común' and dato['espesor']=='0.15 cm':
                nuevo = Pared_Comun(dato['alto'], dato['ancho'])
                nuevo.calculo_PC15()
                descripcion = """
------------------OBI------------------\n
Pared de Ladrillos Comúnes\n
%s de Alto.\n
%s de Ancho.\n
%s de Espesor.\n
------------------------------------------\n""" % (dato['alto'], dato['ancho'], dato['espesor'])
                descripcionh = """
------------------OBI------------------\n<br>
Pared de Ladrillos Comúnes\n<br>
%s de Alto.\n<br>
%s de Ancho.\n<br>
%s de Espesor.\n<br>
------------------------------------------\n<br>""" % (dato['alto'], dato['ancho'], dato['espesor'])

                lista1 = nuevo.detalle
                query = "SELECT precio FROM materiales WHERE id_materiales=1 or id_materiales=2 or id_materiales=3 or id_materiales=7"
            elif dato['tipo']=='Ladrillo Común' and dato['espesor']=='0.20 cm':
                nuevo = Pared_Comun(dato['alto'], dato['ancho'])
                nuevo.calculo_PC20()
                descripcion = """
------------------OBI------------------\n
Pared de Ladrillos Comúnes\n
%s de Alto.\n
%s de Ancho.\n
%s de Espesor.\n
------------------------------------------\n""" % (dato['alto'], dato['ancho'], dato['espesor'])
                descripcionh = """
------------------OBI------------------\n<br>
Pared de Ladrillos Comúnes\n<br>
%s de Alto.\n<br>
%s de Ancho.\n<br>
%s de Espesor.\n<br>
------------------------------------------\n<br>""" % (dato['alto'], dato['ancho'], dato['espesor'])

                lista1 = nuevo.detalle
                query = "SELECT precio FROM materiales WHERE id_materiales=1 or id_materiales=2 or id_materiales=3 or id_materiales=7"
            elif dato['tipo'] =='Ladrillo Común' and dato['espesor'] == '0.30 cm':
                nuevo = Pared_Comun(dato['alto'], dato['ancho'])
                nuevo.calculo_PC30()
                descripcion = """
------------------OBI------------------\n
Pared de Ladrillos Comúnes\n
%s de Alto.\n
%s de Ancho.\n
%s de Espesor.\n
------------------------------------------\n""" % (dato['alto'], dato['ancho'], dato['espesor'])
                descripcionh = """
------------------OBI------------------\n<br>
Pared de Ladrillos Comúnes\n<br>
%s de Alto.\n<br>
%s de Ancho.\n<br>
%s de Espesor.\n<br>
------------------------------------------\n<br>""" % (dato['alto'], dato['ancho'], dato['espesor'])

                lista1 = nuevo.detalle
                query = "SELECT precio FROM materiales WHERE id_materiales=1 or id_materiales=2 or id_materiales=3 or id_materiales=7"
            traer=Conexion()
            precios2=traer.ejecutar_get(query)
            precios=[]
            for item in precios2:
                for element in item:
                    precios.append(int(element))

            #precios = [(10), (7.8), (1450), (4)]
            total = [a * b for a, b in zip(precios, lista1)]
            string = '''
Cal...{0} kg\n
Cemento...{1} kg\n
Arena...{2} m3\n
Ladrillos...{3}\n
------------------------------------------\n
Total...${4}'''.format(round(lista1[0], 2), round(lista1[1], 2), round(lista1[2], 2),round(lista1[3], 2),round(sum(total), 2))
            stringh = '''
Cal...{0} kg\n<br>
Cemento...{1} kg\n<br>
Arena...{2} m3\n<br>
Ladrillos...{3}\n<br>
------------------------------------------\n<br>
Total...${4}<br>'''.format(round(lista1[0], 2), round(lista1[1], 2), round(lista1[2], 2),round(lista1[3], 2),round(sum(total), 2))

            texto = descripcion + string
            textohtm=descripcionh + stringh
            new_p = p.vistaPared(texto, "disable")
            if p.valor=="principal":
                self.levantarVentanaCalculo()
            elif p.valor == "añadir":
                self.totales['pared']=textohtm
                self.levantarVentanaCalculo()
if __name__=="__main__":
    new=Controlador()
    new.validarUsuario()    

#consulta para traer los materiales
#query="SELECT precio FROM materiales WHERE id_materiales=1 or id_materiales=4 or id_materiales=6"
#orden de los materiales en la tabla
#(1, 'cal', 10),
#(2, 'cemento', 7.8),
#(3,'arena',1450),
#(4,'piedra',1100),
#(5,'hierro del 10',850),
#(6,'hierro del 4',450);
#7	Ladrillo Comun 0,15	10
#8	Bloque Ceramico 0,15	10
#9	Bloque Ceramico 0,20	10
#10	bloque de hormigon 0,15	10
#11	bloque de hormigon 0,20	10