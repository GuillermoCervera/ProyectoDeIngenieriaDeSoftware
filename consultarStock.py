#Guillermo Jose Cervera Cervera

#!/usr/bin/python

#Importar el modulo connector para la conexion con mysql
import mysql.connector

#Conectarse a la base de datos
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="distribuidor"
)

#Instanciar un objeto de la clase cursor, lo que permite ejecutar las sentencias SQL
mycursor = mydb.cursor()

#Obtener todas las columnas de la tabla productos
print("Stock actual:")
mycursor.execute("SELECT * FROM productos")

#Recuperar todas las filas en forma de tupla
myresult = mycursor.fetchall()

#Recorrer los registros e imprimirlos en pantalla
for x in myresult:
  print(x)