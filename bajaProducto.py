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

#Eliminar valores en la tabla productos
sql = "DELETE FROM productos WHERE id = '2'"
mycursor.execute(sql)

#Comitear los cambios
mydb.commit()

#Imprimir en pantalla el numero de registros elininados
print(mycursor.rowcount, "record deleted.")