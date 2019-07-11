import pdfkit
from jinja2 import Environment, FileSystemLoader

def generaReporteUnico(datos,nombre=""):
    env = Environment(loader = FileSystemLoader("template"))
    template = env.get_template("reporteunico.html")
    Nombre='%s.pdf' %(nombre)
    
    html = template.render(datos)
    f=open("nuevoUnico.html","w")
    f.write(html)
    f.close()
    config = pdfkit.configuration(wkhtmltopdf="C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe")
    pdfkit.from_file('nuevoUnico.html',Nombre,configuration=config)
    