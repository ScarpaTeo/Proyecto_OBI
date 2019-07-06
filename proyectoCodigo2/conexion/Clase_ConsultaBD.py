import mysql.connector

class Conexion:
    def __init__(self,host="localhost",user="root",passwd="464985",database="obi"):
        self.host=host
        self.user=user
        self.passwd=passwd
        self.database=database
    def conectar(self):
        'crea una conexion con la base de datos '
        self.myBase = mysql.connector.connect(host=self.host,user=self.user,passwd=self.passwd,database=self.database)
        print("se creo la conexion")

    def abrir_cursor(self):
        'aca creo el curso'
        self.mycursor = self.myBase.cursor()
        print("se abrio el cursor")

    def ejecutar_consulta(self,query,values=''):
        'aca creo la consulta mysql'
        self.mycursor.execute(query,values)
        print("se ejecuto la consulta")

    def traer_datos(self):
        """Traer registros"""
        self.resultado = self.mycursor.fetchall()
        print("se trajeron los archivos")
        return self.resultado
    def enviar_commit(self,query):
        'enviar commit a la base de datos '
        consulta=query.lower()
        es_lectura=consulta.count('select')
        if es_lectura < 1:
            self.myBase.commit()
    def cerrar_cursor(self):
        'aca cerramos el cursos una vez ejecutada la consulta a la base'
        self.mycursor.close()

    #el metodo mas importante, el que va a Unitodo junto
    def ejecutar_set(self,consulta,valores=''):
        'llama a todos los metodos para hacer un Set a la base'
        datos=False
        if (self.host and self.user and self.passwd and self.database and consulta):
            self.conectar()
            self.abrir_cursor()
            self.ejecutar_consulta(consulta,valores)
            self.enviar_commit(consulta)
            self.cerrar_cursor()
            datos=True
        return datos
    def ejecutar_get(self,consulta,valores=''):
        'llama a todos los metodos para hacer un GET desde la base'
        datos=""
        if (self,self.host and self.user and self.passwd and self.database and consulta):
            self.conectar()
            self.abrir_cursor()
            self.ejecutar_consulta(consulta,valores)
            datos=self.traer_datos()
            self.cerrar_cursor()
        return datos

#----------------------------------------Consulta de prueba Cargar campos SET a la base
'''
patente=input("ingresa la patente:\n")
nombre=input("ingresa el nombre:\n")
apellido=input("ingresa el apellido:\n")
dni=int(input("ingresa el Dni:\n"))
saldo=float(input("ingresa el saldo:\n"))

sql="INSERT INTO usuario(usuario,contraseña,confirmar_contraseña,email,nombre_completo) VALUES (%s,%s,%s,%s,%s)"
valores=("teo","123","123","teo@gmail.com","teo Scarpa")
nuevo=Conexion()
nuevo.ejecutar_set(sql,valores)'''
#----------------------------------------Consulta de prueba GET a la base

#patente=''
#patente=input("ingrese la patente: \n")
#sql2="SELECT * FROM registro WHERE Patente='{0}'".format(patente)
"""sql2="SELECT * FROM usuario WHERE usuario='nicolas' AND contraseña='123'"
print(sql2)

nueva=Conexion()
x=nueva.ejecutar_get(sql2)
dato=x[0]
print(dato[1])"""

#---------------------------------------Consulta actualizar valores en la Base
"""sql3="UPDATE usuario SET usuario=%s WHERE contraseña=%s ;"
datos=("nicolass",'123')

actualizar=Conexion()
actualizar.ejecutar_set(sql3,datos)
"""