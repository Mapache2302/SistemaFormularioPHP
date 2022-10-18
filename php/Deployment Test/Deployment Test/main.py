#Liberias necesarias
from flask import Flask
from flask import render_template #Renderizado 
from flask import request
from werkzeug.exceptions import HTTPException, NotFound
from pymysql.err import IntegrityError
from flaskext.mysql import MySQL #Conexión con la base de datos MySQL
from flask import Flask, request, make_response
from flask_sqlalchemy import SQLAlchemy
import os
import sqlalchemy
from google import auth
import sys
from google.cloud.sql.connector import Connector
import sqlalchemy
from sqlalchemy import text
import smtplib

formulario = Flask(__name__, template_folder='www') 

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "www/glassy-totality-365703-ca64820d4061.json"

INSTANCE_CONNECTION_NAME = "glassy-totality-365703:us-central1:formdb" # i.e demo-project:us-central1:demo-instance
DB_USER = "root"
DB_PASS = "123"
DB_NAME = "epgWebPageDB"

# initialize Connector object
connector = Connector()

# function to return the database connection object
def getconn():
    conn = connector.connect(
        INSTANCE_CONNECTION_NAME,
        "pymysql",
        user=DB_USER,
        password=DB_PASS,
        db=DB_NAME
    )
    return conn

# create connection pool with 'creator' argument to our connection object function
pool = sqlalchemy.create_engine(
    "mysql+pymysql://",
    creator=getconn,
)

from xml import dom


class e_mail():
    def __init__(self):
        print("¡Preparando un e-mail!")

    def setData(self, data):
        self.source = data[0]
        self.password = data[1]
        self.dest = data[2]

    def setMessage(self, subject, content):
        self.message = 'Subject: {} \n\n {}'.format(subject, content)
    
    def sentEmail(self): # Data = (CorreoEmisor, Password, CorreoReceptor, Mensaje)
        
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(self.source, self.password)
        server.sendmail(self.source, self.dest, self.message.encode('utf-8'))
        server.quit()
   
        print("¡Correo enviado exitosamente!")

class AlumnoOBJ:
    
    def __init__(self):
        print("¡Se ha seleccionado a un alumno!")
    
    def setData(self, data):
        self.CodAlumno =data[0][0]
        self.NombreAlumno = data[0][1]
        self.Correo = data[0][2]
    
    def setCode(self, data):
        self.CodAlumno = data

    def setNombreAlumno(self, data):
        self.NombreAlumno =data

    def setCorreo(self, data):
        self.Correo=data

    def getCode(self):
        return self.CodAlumno

    def getFullName(self):
        return self.NombreAlumno
    
    def getCorreo(self):
        return self.Correo

    def printData(self):
        print("El código del alumno es: ", self.CodAlumno)
        print("El Nombre del alumno es: ", self.NombreAlumno)
        print("El Correo del alumno es: ", self.Correo)
        

class Resultado_FormularioOBJ:
    def __init__(self):
        self.p1 = 1 #Peso Originalidad
        self.p2 = 1 #Peso Importancia
        self.p3 = 1 #Peso Coherencia
        self.p4 = 1 #Peso Metodología
        self.p5 = 1 #Peso Validez
        self.p6 = 1 #Peso Dominio
    
    def setData(self, data):
        self.code = data[0]
        self.originalidad = data[1]
        self.importancia = data[2]
        self.coherencia = data[3]
        self.metodologia = data[4]
        self.validez = data[5]
        self.dominio = data[6]
        self.recomendacion = data[7]
    
    def printData(self):
        print("Código de alumno: ", self.code)
        print("Originalidad: ", self.originalidad)
        print("Importancia: ", self.importancia)
        print("Coherencia: ", self.coherencia)
        print("Metodología: ", self.metodologia)
        print("Validez: ", self.validez)
        print("Dominio: ", self.dominio)
        print("Recomendación: ", self.recomendacion)

    def getProm(self):
        dividendo = (self.originalidad * self.p1) + (self.importancia * self.p2) + (self.coherencia * self.p3) + (self.metodologia * self.p4) + (self.validez * self.p5) + (self.dominio * self.p6)
        divisor = (self.p1 + self.p2 + self.p3 + self.p4 + self.p5 + self.p6)
        return dividendo/divisor

    def getData(self):
        prom = self.getProm()
        code = self.code
        originalidad = self.originalidad
        importancia = self.importancia
        coherencia = self.coherencia
        metodologia = self.metodologia
        validez = self.validez
        dominio = self.dominio
        recomendacion = self.recomendacion 
        data = (code, originalidad, importancia, coherencia, metodologia, validez, dominio, recomendacion, prom)
        return data

#Alumno - Almacena información. 
newAlumn = AlumnoOBJ()
#Resultado_Formulario  - Almacena informacións
newResult = Resultado_FormularioOBJ()

import email
from hashlib import new
import smtplib



# Prueba
#_data = ('rsoles@unitru.edu.pe', 'trujillo2010', 'renzoarturo12345@gmail.com')
#newEmail = e_mail()
#newEmail.setData(_data)
#subject = 'Prueba'
#content = '¡Prueba!'
#newEmail.getMessage(subject, content)
#newEmail.sentEmail()

 #Route
@formulario.route('/') #Podrá recibir solicitudes mediante la URL 
def index():
    return render_template('index.html') #Dirección del archivo html.


@formulario.route('/alumnos', methods=['POST'])
def alumnos():

    try:
        with pool.connect() as db_conn:
            db_conn.execute(
            "CREATE TABLE IF NOT EXISTS alumnos "
            "(CodAlumno VARCHAR(15),"
            "nombreAlumno VARCHAR(60),"
            "correo VARCHAR(60),"
            "PRIMARY KEY (CodAlumno));"
            )
            _codAlumno = request.form['codigoAlumno']
            search = sqlalchemy.text("SELECT * FROM alumnos WHERE CodAlumno=:cod;",)
            result = db_conn.execute(search, cod=_codAlumno).fetchall()
            newAlumn.setData(result)
            newAlumn.printData()
            NombreCompleto = newAlumn.getFullName()    
            NombreCompleto = NombreCompleto + " - " + newAlumn.getCode()
    except:
        print("¡ERROR!")
        return render_template('index.html', NombreCompleto = "¡Código incorrecto, ingrese nuevamente!")

    return render_template('index.html', NombreCompleto = NombreCompleto)    


@formulario.route('/store', methods=['POST'])
def store():
    try:
    
       _originalidad = int(request.form['originalidad'])
       _importancia = int(request.form['importancia'])
       _coherencia = int(request.form['coherencia'])
       _metodologia = int(request.form['metodologia'])
       _validez = int(request.form['validez'])
       _dominio = int(request.form['dominio'])
       _recomendaciones = request.form['recomendaciones']
       code = newAlumn.getCode()
       

       # Modificar objeto
       _data = (code, _originalidad, _importancia, _coherencia, _metodologia, _validez, _dominio, _recomendaciones)
       newResult.setData(_data)
       prom = newResult.getProm()
              
    except HTTPException as e:
       print("¡Error!")
       print(e)
       return render_template('index.html')
    
    try:
       
       originalidad = str(_originalidad)
       importancia = str(_importancia)
       coherencia = str(_coherencia)
       metodologia = str(_metodologia)
       validez = str(_validez)
       dominio = str(_dominio)

       with pool.connect() as db_conn:
            # create ratings table in our movies database
           
        
            db_conn.execute(
                    "CREATE TABLE IF NOT EXISTS resultado_formulario "
                    "(codAlumno VARCHAR(15), Pregunta1 int,Pregunta2 int,Pregunta3 int,"
                    "Pregunta4 int,Pregunta5 int,Pregunta6 int,Recomendacion VARCHAR(250),promedio float,"
                    "PRIMARY KEY (codAlumno));"
            )
            # insert data into our ratings table
            insert_stmt = sqlalchemy.text(
                "INSERT INTO resultado_formulario (codAlumno, Pregunta1, Pregunta2, Pregunta3, Pregunta4, Pregunta5, Pregunta6, Recomendacion, promedio) VALUES (:codAlumno, :Pregunta1, :Pregunta2, :Pregunta3, :Pregunta4, :Pregunta5, :Pregunta6, :Recomendacion, :promedio);",
            )

            # insert entries into table
            db_conn.execute(insert_stmt, codAlumno=code, Pregunta1=_originalidad, Pregunta2=_importancia, Pregunta3=_coherencia, Pregunta4=_metodologia, Pregunta5=_validez, Pregunta6=_dominio, Recomendacion=_recomendaciones, promedio=prom)
       

       print("¡Se enviarán los resultados al correo del alumno!")
       
       source = "rsoles@unitru.edu.pe"
       password = "trujillo2010"
       _dataEmail = (source, password, newAlumn.getCorreo())

       newEmail = e_mail()
       newEmail.setData(_dataEmail)
      

       #Formato MSG
       subject = "Resultado de la prueba del alumno: " + " " + newAlumn.getFullName()
       content = "¡Saludos querido alumno!, nos comunicamos para darle a conocer los resultados de su prueba de evaluación.\n\n Estos son: \n\n ORIGINALIDAD: {} \n\n IMPORTANCIA: {} \n\n COHERENCIA: {} \n\n METODOLOGÍA: {} \n\n VALIDEZ DE RESULTADOS Y CONDICIONES: {} \n\n DOMINIO DEL TEMA: {} \n\n El promedio que obtuvo es: {} \n Se le recomienda: {}".format(originalidad, importancia, coherencia, metodologia, validez, dominio, prom, _recomendaciones)  
   
       newEmail.setMessage(subject, content)
       newEmail.sentEmail()
 


    except IntegrityError as e:
       print("¡Error de integridad!")
       print(e)


    return render_template('index.html')    

if __name__ == '__main__':
    formulario.run(debug=True)

