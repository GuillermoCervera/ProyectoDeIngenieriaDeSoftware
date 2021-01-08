# Guillermo Cervera

import mysql.connector

class Productos:

    def abrir(self):
        conexion=mysql.connector.connect(host="localhost", user="root", passwd="", database="DISTRIBUIDOR")
        return conexion

    def alta(self, datos):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="insert into PRODUCTO(NOMBRE_PRODUCTO, CANTIDAD_PRODUCTO) values (%s,%s)"
        cursor.execute(sql, datos)
        cone.commit()
        cone.close()
    
    def lista_todos(self):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="select CODIGO_PRODUCTO, NOMBRE_PRODUCTO, CANTIDAD_PRODUCTO from PRODUCTO"
        cursor.execute(sql)
        return cursor.fetchall()

    def consulta(self, datos):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="select CODIGO_PRODUCTO, NOMBRE_PRODUCTO, CANTIDAD_PRODUCTO from PRODUCTO where NOMBRE_PRODUCTO=%s"
        cursor.execute(sql, datos)
        return cursor.fetchall()

    def modificacion(self, datos):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="update PRODUCTO set NOMBRE_PRODUCTO=%s, CANTIDAD_PRODUCTO=%s where CODIGO_PRODUCTO=%s"
        cursor.execute(sql, datos)
        cone.commit()
        #cone.close()
        return cursor.rowcount

    def baja(self, datos):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="delete from PRODUCTO where NOMBRE_PRODUCTO=%s"
        cursor.execute(sql, datos)
        cone.commit()
        cone.close()
        return cursor.rowcount