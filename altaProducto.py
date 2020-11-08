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

#Insertar valores en la tabla productos
sql = "INSERT INTO productos (id, nombre, cantidad) VALUES (%s, %s, %s)"
val = ("2", "bebida2", "100")
mycursor.execute(sql, val)

#Comitear los cambios
mydb.commit()

#Imprimir en pantalla el numero de registros insertados
print(mycursor.rowcount, "record inserted.")