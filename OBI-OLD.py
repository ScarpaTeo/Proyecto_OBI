'''
Created on 23 sep. 2018

@author: TEO
'''

from math import pi
import sys
from io import open
from builtins import int
archivo_texto=open("detalle_materiales.txt","w")
####################################################CALCULOS DE SUPERFICIE Y LLAMADA A FUNCIONES
def calculo_cubico():
    cadena="""*************************usted necesita cubir %s metros cubicos*************************\n
    Largo: %s m. \n
    Alto: %s m. \n
    Ancho: %s m. \n
---------------------------------------------------detalle de materiales:\n"""
    print("""elegiste calcular cimientos!\n...................................................................\n
    Opciones Disponibles:\n
    1.zapata corrida de Hormigon\n
    2.viga de Fundacion\n
    3.pilotines\n
    4.Contrapiso\n
    *nota:se te van a pedir las medidas de lo que queres calular, si queres calcular pilotines ingresa ceros ya que es un calculo diferente*\n""")
    lado1=float(input("ingresa el largo\n"))
    lado3=float(input("ingresa el ancho o espesor \n"))
    lado2=float(input("ingresa el alto o profundidad \n"))
    cubico=round(lado1*lado2*lado3)
    print(cadena%(cubico,lado1,lado2,lado3))
    archivo_texto.write(cadena%(cubico,lado1,lado2,lado3))
    op=int(input("""ingrese el numero de la opcion que desea calcular\n...................................................................\n"""))
    if op ==1:
        calculo_zapataCo(cubico)
    elif op==2:
        calculo_vigaencadenado(cubico)
    elif op ==3:
        calculo_pilotines()
    elif op==4:
        Calculo_carpetas(cubico)
    
    else:
        print("opcion equivocada, intente de nuevo")
        calculo_cubico()
def calculo_cuadrado():
    cadena="""*************************usted necesita cubir %s metros cuadrados*************************\n
    Largo: %s m. \n
    Alto: %s m. \n
    --------------------------------------------------detalle de materiales:\n"""
    lado1=float(input("ingresa el largo\n"))
    lado2=float(input("ingresa el alto\n"))
    cuadrado=round(lado1*lado2)
    print(cadena%(cuadrado,lado1,lado2))
    archivo_texto.write(cadena%(cuadrado,lado1,lado2))
    print("""puede elegir calcular\n...................................................................\n
    1.pared de ladrillo comun\n 
    2.pared de bloques\n 
    3.pared de tabiques""")
    op=int (input("ingrese el numero de la opcion que desea calcular\n...................................................................\n"))
    if op ==1:
        calculo_paredComun(cuadrado)
    elif op==2:
        calculo_paredBloques(cuadrado)
    elif op ==3:
        calculo_paredTabiques(cuadrado)
    else:
        print("opcion equivocada , intente de nuevo")
        calculo_cuadrado()
#######################################################CALCULOS DE CIMIENTOS
def calculo_pilotines():
    cadena="""****para hacer una cantidad de %s pilotines de Hormigon de %s de diametro y profundidad %s mts*******\n
    dosificacion H°C... 1:3:3 \n
    va a necesitar de cemento....%s kg \n
    va a necesitar de arena....%s m3 \n
    va a necesitar de piedra....%s m3 \n
    va a necesitar de hierros del 10....%s m \n
    va a necesitar de hierros del 4.....%s m \n
    ----------------------------------------------\n"""
    diametro=float(input("ingrese el diametro que desea utilizar \n "))
    profundidad=float(input("Ingrese la profundidad del pilotin\n "))
    cantidad=int(input("ingrese la cantidad de pilotines que va a necesitar ...\n"))
    dato=pi*(diametro/2)*profundidad
    
    cemento = "{0:.2f}".format(14.70*dato*cantidad)
    arena ="{0:.2f}".format(0.32*dato*cantidad)
    piedra ="{0:.2f}".format(0.32*dato*cantidad)
    hierro10="{0:.2f}".format(5.5*dato*cantidad)
    hierro4="{0:.2f}".format(3.50*dato*cantidad)
    print(cadena%(cantidad,diametro,profundidad,cemento,arena,piedra,hierro10,hierro4))
    archivo_texto.write(cadena%(cantidad,diametro,profundidad,cemento,arena,piedra,hierro10,hierro4))
    
    seguir_salir()   
##################################
def calculo_zapataCo(y):
    cadena="""****para hacer cimiento el corrido de Hormigon*******\n
    va a necesitar de cal....%s kg \n
    va a necesitar de cemento....%s kg \n
    va a necesitar de arena....%s m3 \n
    va a necesitar de piedra....%s m3 \n
    -----------------------------\n
    dosificacion con Hercal .......1:4:8 \n
    va a necesitar de hercal....%s kg \n
    va a necesitar de arena....%s m3 \n
    va a necesitar de piedra....%s m3 \n"""
    cal = "{0:.2f}".format(81*y)
    cemento ="{0:.2f}".format(38.40*y)
    arena ="{0:.2f}".format(0.51*y)
    cascote ="{0:.2f}".format(0.77*y)
    hercal="{0:.2f}".format(105*y)
    arena ="{0:.2f}".format(0.45*y)
    cascote ="{0:.2f}".format(0.9*y)
    
    print(cadena%(cal,cemento,arena,cascote,hercal,arena,cascote))
    archivo_texto.write(cadena%(cal,cemento,arena,cascote,hercal,arena,cascote))
    seguir_salir()
################################
def calculo_vigaencadenado(y):
    cadena="""****para hacer la viga de encadenado*******\n
    va a necesitar de cemento....%s kg \n
    va a necesitar de arena....%s m3 \n
    va a necesitar de piedra....%s m3 \n
    va a necesitar de hierros del 10....%s m \n
    va a necesitar de hierros del 4.....%s m \n""" 
    cemento ="{0:.2f}".format(12*y)
    arena ="{0:.2f}".format(0.26*y)
    piedra ="{0:.2f}".format(0.26*y)
    hierro10="{0:.2f}".format( 4*y)
    hierro4="{0:.2f}".format(3.50*y)
    print(cadena%(cemento,arena,piedra,hierro10,hierro4))
    archivo_texto.write(cadena%(cemento,arena,piedra,hierro10,hierro4))
    seguir_salir()
    
#########}###########################CALCULO DE PAREDES
def calculo_paredTabiques(y):
    print("elegiste calcular una pared de Ladrillos huecos\n----------------\n")
    print("puedes elegir entre\nopcion 1: pared de 0.10 \nopcion 2: pared de 0.20")
    op=int(input("ingrese su opcion\n----------------\n"))
    if op == 1:
        cadena="""****elegiste pared de tabiques de 0.10!*******\n
    va a necesitar de cal....%s kg \n
    va a necesitar de cemento....%s kg \n
    va a necesitar de arena....%s m3 \n
    va a necesitar %s bloques \n""" 
        cal="{0:.2f}".format(3.4*y)
        cemento="{0:.2f}".format(3.5*y)
        arena="{0:.2f}".format(0.16*y)
        bloques="{0:.2f}".format(30*y)
        print(cadena%(cal,cemento,arena,bloques))
        archivo_texto.write(cadena%(cal,cemento,arena,bloques))
        seguir_salir()
    elif op == 2:
        cadena="""****elegiste pared de tabiques de 0.20!*******\n
    va a necesitar de cal....%s kg \n
    va a necesitar de cemento....%s kg \n
    va a necesitar de arena....%s m3 \n
    va a necesitar %s bloques \n"""
        cal="{0:.2f}".format(7.8*y)
        cemento="{0:.2f}".format(8*y)
        arena="{0:.2f}".format(0.37*y)
        bloques="{0:.2f}".format(33*y)
        print(cadena%(cal,cemento,arena,bloques))
        archivo_texto.write(cadena%(cal,cemento,arena,bloques))
        seguir_salir()
    else:
        print("opcion incorrecta , intenta de nuevo")
        calculo_paredTabiques(y)

###############################################
def calculo_paredBloques(y):
    print("elegiste calcular una pared de Ladrillos de bloques\n----------------\n")
    print("puedes elegir entre\nopcion 1: bloques ceramicos\nopcion 2: bloques de cemento")
    op=int(input("ingrese su opcion\n----------------\n"))
    if op == 1:
        print("elegiste pared de bloques ceramicos\n----------------\n")
        print("podes elegir entre: \n 1.pared de 0.15\n 2.pared de 0.20")
        opcion=int(input("ingrese su opcion\n"))
        if opcion ==1:
            cadena="""****elegiste pared de bloques ceramico de 0.15!*******\n
    va a necesitar de cal....%s kg \n
    va a necesitar de cemento....%s kg \n
    va a necesitar de arena....%s m3 \n
    va a necesitar %s bloques \n"""
            cal="{0:.2f}".format(2.5*y)
            cemento="{0:.2f}".format(0.65*y)
            arena="{0:.2f}".format(0.12*y)
            bloques="{0:.2f}".format(12.5*y)
            print(cadena%(cal,cemento,arena,bloques))
            archivo_texto.write(cadena%(cal,cemento,arena,bloques))
            seguir_salir()
        if opcion==2:
            cadena="""****elegiste pared de bloques ceramico de 0.20!*******\n
    va a necesitar de cal....%s kg \n
    va a necesitar de cemento....%s kg \n
    va a necesitar de arena....%s m3 \n
    va a necesitar %s bloques \n"""
            cal="{0:.2f}".format(3*y)
            cemento="{0:.2f}".format(0.78*y)
            arena="{0:.2f}".format(0.15*y)
            bloques="{0:.2f}".format(12.5*y)
            print(cadena%(cal,cemento,arena,bloques))
            archivo_texto.write(cadena%(cal,cemento,arena,bloques))
            seguir_salir()
    elif op ==2:
        print("elegiste pared de bloques  de hormigon\n----------------\n")
        print("podes elegir entre: \n 1.pared de 0.10\n 2.pared de 0.20")
        opcion=int(input("ingrese su opcion\n"))
        if opcion ==1:
            cadena="""****elegiste pared de bloques de hormigon 0.10!*******\n
    va a necesitar de cal....%s kg \n
    va a necesitar de cemento....%s kg \n
    va a necesitar de arena....%s m3 \n
    va a necesitar %s bloques \n"""
            cal="{0:.2f}".format(1.9*y)
            cemento="{0:.2f}".format(1.95*y)
            arena="{0:.2f}".format(0.13*y)
            bloques="{0:.2f}".format(12.5*y)
            print(cadena%(cal,cemento,arena,bloques))
            archivo_texto.write(cadena%(cal,cemento,arena,bloques))
            seguir_salir()
        elif opcion==2:
            cadena="""****elegiste pared de bloques de hormigon 0.20!*******\n
    va a necesitar de cal....%s kg \n
    va a necesitar de cemento....%s kg \n
    va a necesitar de arena....%s m3 \n
    va a necesitar %s bloques \n"""
            cal="{0:.2f}".format(1.5*y)
            cemento="{0:.2f}".format(3.30*y)
            arena="{0:.2f}".format(0.15*y)
            bloques="{0:.2f}".format(12.5*y)
            print(cadena%(cal,cemento,arena,bloques))
            archivo_texto.write(cadena%(cal,cemento,arena,bloques))
            seguir_salir()
    else:
        print("opcion, incorrecta ,intenta nuevamente")
        calculo_paredBloques(y)

#################################################
def calculo_paredComun(y):
    print("elegiste calcular una pared de Ladrillos comunes!")
    print("puedes elegir entre\n----------------\nopcion 1: pared de 15cm")
    print("opcion 2: pared de 20cm\nopcion 3:pared de 30cm")
    op=int(input("ingrese su opcion\n----------------\n"))
    if op == 1:
        cadena="""****elegiste pared de ladrillos comunes de 0.15!*******\n
    va a necesitar de cal....%s kg \n
    va a necesitar de cemento....%s kg \n
    va a necesitar de arena....%s m3 \n
    va a necesitar %s ladrillos \n"""
        cal="{0:.2f}".format(7.3*y)
        cemento="{0:.2f}".format(7.5*y)
        arena="{0:.2f}".format(0.35*y)
        ladrillos="{0:.2f}".format(60*y)
        print(cadena%(cal,cemento,arena,ladrillos))
        archivo_texto.write(cadena%(cal,cemento,arena,ladrillos))
        seguir_salir()

    elif op ==2:
        cadena="""****elegiste pared de ladrillos comunes de 0.20!*******\n
    va a necesitar de cal....%s kg \n
    va a necesitar de cemento....%s kg \n
    va a necesitar de arena....%s m3 \n
    va a necesitar %s ladrillo \n"""
        cal="{0:.2f}".format(13.20*y)
        cemento="{0:.2f}".format(6.9*y)
        arena="{0:.2f}".format(0.65*y)
        ladrillos="{0:.2f}".format(90*y)
        print(cadena%(cal,cemento,arena,ladrillos))
        archivo_texto.write(cadena%(cal,cemento,arena,ladrillos))
        seguir_salir()
    elif op ==3:
        cadena="""****elegiste pared de ladrillos comunes de 0.30!*******\n
    va a necesitar de cal....%s kg \n
    va a necesitar de cemento....%s kg \n
    va a necesitar de arena....%s m3 \n
    va a necesitar %s ladrillos \n"""
        cal="{0:.2f}".format(19.10*y)
        cemento="{0:.2f}".format(9.90*y)
        arena="{0:.2f}".format(0.90*y)
        ladrillos="{0:.2f}".format(120*y)
        print(cadena%(cal,cemento,arena,ladrillos))
        archivo_texto.write(cadena%(cal,cemento,arena,ladrillos))
        seguir_salir()
    else:
        print("opcion incorrecta, intenta nuevamente")
        calculo_paredComun(y)
########################################REVOQUES Y CONTRAPISOS
def Calculo_carpetas(y):
    print("""puede elegir calcular: \n
    1.Revoques
    2.contrapiso""")
    op=int(input("************ ingrese su opcion *****************\n"))
    if op==1:
        print("""op1:Revoque completo exterior\n
        op2:Revoque completo interior\n""")
        elegido=int(input("ingrese su opcion\n"))
        if elegido==1:
            cadena="""****para hacer %s mts cubicos de revoque completo exterior*******\n
        --------------------------------------Azotado Hidrofugo\n
        va a necesitar de cemento....%s kg \n
        va a necesitar de arena....%s m3 \n
        *Hidrofugo al 10 porciento del agua del mortero*\n
        ----------------------------------------------------Revoque grueso\n
        va a necesitar de cal....%s kg \n
        va a necesitar de cemento....%s kg \n
        va a necesitar de arena....%s m3 \n
        ------------------------------------------------Revoque fino\n
        va a necesitar de cal aerea....%s kg \n
        va a necesitar de cemento....%s kg \n
        va a necesitar de arena....%s m3 \n
        """ 
            cemento_hidro ="{0:.2f}".format(2.7*y)
            arena_hidro ="{0:.2f}".format(0.06*y)
            
            cemento_gru ="{0:.2f}".format(1.85*y)
            arena_gru ="{0:.2f}".format(0.17*y)
            cal_gru="{0:.2f}".format(3.6*y)
            
            cemento_fi ="{0:.2f}".format(0.45*y)
            arena_fi ="{0:.2f}".format(0.06*y)
            cal_fi="{0:.2f}".format(1.6*y)
            print(cadena%(y,cemento_hidro,arena_hidro,cal_gru,cemento_gru,arena_gru,cal_fi,cemento_fi,arena_fi))
            archivo_texto.write(cadena%(y,cemento_hidro,arena_hidro,cal_gru,cemento_gru,arena_gru,cal_fi,cemento_fi,arena_fi))
            seguir_salir()
            
        elif elegido==2:
            cadena="""****para hacer %s mts cubicos de revoque completo interior*******\n
        ----------------------------------------------------Revoque grueso\n
        va a necesitar de cal....%s kg \n
        va a necesitar de cemento....%s kg \n
        va a necesitar de arena....%s m3 \n
        ------------------------------------------------Revoque fino\n
        va a necesitar de cal aerea....%s kg \n
        va a necesitar de cemento....%s kg \n
        va a necesitar de arena....%s m3 \n
        """ 
            cemento_hidro ="{0:.2f}".format(2.7*y)
            arena_hidro ="{0:.2f}".format(0.06*y)
            
            cemento_gru ="{0:.2f}".format(1.85*y)
            arena_gru ="{0:.2f}".format(0.17*y)
            cal_gru="{0:.2f}".format(3.6*y)
            
            cemento_fi ="{0:.2f}".format(0.45*y)
            arena_fi ="{0:.2f}".format(0.06*y)
            cal_fi="{0:.2f}".format(1.6*y)
            print(cadena%(y,cal_gru,cemento_gru,arena_gru,cal_fi,cemento_fi,arena_fi))
            archivo_texto.write(cadena%(y,cal_gru,cemento_gru,arena_gru,cal_fi,cemento_fi,arena_fi))
            seguir_salir()
                
        else:
            print("ingresaste una opcion incorrecta, intenta de nuevo")
            Calculo_carpetas(y)
    elif op==2:
        cadena="""
        ****para hacer %s mts cubicos de Contrapiso*******\n
        va a necesitar de cal....%s kg \n
        va a necesitar de cemento....%s kg \n
        va a necesitar de arena....%s m3 \n
        va a necesitar de cascote....%s m3 \n
        ----------------------------------------------------\n
        con cemento de albanileria: \n
        va a necesitar de cemento albanileria....%s kg \n
        va a necesitar de arena....%s m3 \n
        va a necesitar de cascote....%s m3 \n""" 
        cemento ="{0:.2f}".format(38.4*y)
        arena ="{0:.2f}".format(0.51*y)
        cascote="{0:.2f}".format(0.77*y)
        cemento_alba="{0:.2f}".format( 105*y)
        cascote2="{0:.2f}".format(0.90*y)
        cal="{0:.2f}".format(81*y)
        print(cadena%(y,cal,cemento,arena,cascote,cemento_alba,arena,cascote2))
        archivo_texto.write(cadena%(y,cal,cemento,arena,cascote,cemento_alba,arena,cascote2))
        seguir_salir()
        
    else:
        print("opcion incorrecta, intenta de nuevo")
        Calculo_carpetas(y)
        
##############################################################CALCULO TECHO CHAPA/LOSA        
def calculo_techo():
    ancho=float(input("ingrese el ancho a cubrir...\n "))
    largo=float(input("ingrese el largo a cubir... \n"))
    dato1=max(ancho,largo)
    dato2=min(ancho,largo)
    dato5=ancho*largo
    
    op=int(input("""******************puede elegi*********************\n
    op1: calcular Correas o tirantes estructurales\n
    op2: calcuar Cantidad de Chapas\n
    """))
    if op==1:
        cadena="""
****los tirantes necesarios para cubrir un largo de %s y un ancho de %s *******\n
va a necesitar %s colocandolos con una separacion de %s\n""" 
        separacion=float(input("ingrese la separacion entre tirantes que desea, teniendo en cuenta que los mas comun es [0.80-1-1.20-1.50]"))
        dato3=dato1-separacion*2
        dato3a="{0:.2f}".format(dato3)
        dato4=dato3/separacion
        dato4a="{0:.2f}".format(dato4)
        total=dato4+2
        totala="{0:.2f}".format(total)
        print(cadena%(largo,ancho,totala,separacion))
        archivo_texto.write(cadena%(largo,ancho,totala,separacion))
        seguir_salir()
    
    elif op==2:
        cadena2="""
****las chapas necesarios para cubrir un largo de %s y un ancho de %s *******\n
va a necesitar %s colocandolas las ondas y la pendiente en el sentido mas largo de la contruccion, con un solape de 0.15 entre chapas\n""" 
        chapa=float(input("""
        ingrese la medida de las chapas que desea utilizar, 
        teniendo en cuenta que los largos comerciales son:\n
        [1.83-2.13-2.44-2.74-3.05-3.36-3.66-3.96] por 1 metro de ancho\n"""))
        dato6=dato5/chapa
        dato7="{0:.2f}".format(dato6)
        print(cadena2%(largo,ancho,dato7))
        archivo_texto.write(cadena2%(largo,ancho,dato7))
        seguir_salir()
###################################################MENU PRINCIPAL
def saludo_menu():
    print("*********bienvenido a OBI*************created by Teo Scarpa")
    print("""esta aplicacion te permitira:\n
    1. calcular cimientos\n 
    2.calcular paredes\n 
    3.calcular contrapisos/revoques\n
    4.calcular techos\n""")
    s=int(input("*********ingrese una opcion*********\n...................................................................\n"))
    if s ==1:
        calculo_cubico()
    elif s ==2:
        calculo_cuadrado()
    elif s==3:
        calculo_cubico()
    elif s==4:
        calculo_techo()
    else:
        print ("ingresaste una opcion equivocada , intenta de nuevo")
        saludo_menu()
        
        
def seguir_salir():
    print("""*******************************************************************************************\n
Desea realizar otro calculo\n
opcion 1: Si.\n
Opcion 2: No.\n""")
    op=int(input())
    if op==1:
        saludo_menu()
    else:
        print("Adios!")
        sys.exit()
########################################################################LLAMADA A FUNCIONES 
saludo_menu()

archivo_texto.close()

