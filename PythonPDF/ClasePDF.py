# para que esto les funque tiene que instalar ( python -m pip install fpdf )

#clase que crea PDF con strings------------------------

class PDF:
    def __init__(self,lista,nombreArchivo):
        self.lista=lista
        self.nombre=nombreArchivo
    def cratePdf(self):
        from fpdf import FPDF
        pdf = FPDF(orientation='p', unit='mm',format='letter')
        pdf.add_page()
        pdf.set_font("Arial", size=14)
        pdf.cell(200,10, txt='%s'%(self.lista), ln=1 , align='c')
        pdf.output("%s.pdf"%(self.nombre))
#-----------------------------------------------------------
nueva=["cemento 100kg , cal 200 kg , arenita 5 M3","otra cosa",1234,"hola mundo"]

#se intancia la clase PDF y se le pasa , una lista con valores y un nombre para el archivo
#que se va a crear

x=PDF(nueva,"detalleObi")
x.cratePdf()

