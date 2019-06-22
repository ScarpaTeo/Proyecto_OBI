import sys
sys.path.append('../vista')
from calculo import calculo

class calculoController():
    ca=calculo()
    def verCimiento(self):
        self.ca.cimiento()
    def verRevoque(self):
