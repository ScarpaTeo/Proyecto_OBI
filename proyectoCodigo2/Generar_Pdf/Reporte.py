import pdfkit
from jinja2 import Environment, FileSystemLoader

def generaReporte(datos,nombre=""):
    print(datos)
    print(nombre)
    env = Environment(loader = FileSystemLoader("template"))
    template = env.get_template("reporte.html")
    Nombre='%s.pdf' %(nombre)
    
    html = template.render(datos)
    f=open("nuevo.html","w")
    f.write(html)
    f.close()
    config = pdfkit.configuration(wkhtmltopdf="C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe")
    pdfkit.from_file('nuevo.html',Nombre,configuration=config)
    