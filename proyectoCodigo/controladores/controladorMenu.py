#controlador de pantalla menu
import sys
sys.path.append('../vista')
import Menu
import PrincipalController

class Menu_controller:

    def __del__(self):
        print("objeto eliminado")


    def levantar(self):
        men=Menu()
        men.MostrarMenu.mostrar()
        sys.exit()

    def llamar_principal(self):
        main=ControllerPrincipal.levantarVentanaCalculo()
        sys.exit()