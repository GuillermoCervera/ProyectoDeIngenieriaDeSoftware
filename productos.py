#Guillermo Cervera

import mysql.connector

class Productos:

    def abrir(self):
        conexion=mysql.connector.connect(host="localhost", user="root", passwd="", database="DISTRIBUIDOR")
        return conexion

    def alta(self, datos):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="insert into PRODUCTO(NOMBRE_PRODUCTO, CANTIDAD_PRODUCTO) values (%s,%s)"
        #sql2="insert into MOVIMIENTO(NOMBRE_PRODUCTO_MOVIMIENTO=%s, CANTIDAD_PRODUCTO_MOVIMIENTO=%s, CODIGO_CABECERA=%s, FECHA_MOVIMIENTO=%s) values(%s,%s,%s,%s)"
        #sql2="insert into MOVIMIENTO(CODIGO_TIPO_MOVIMIENTO=1, NOMBRE_PRODUCTO_MOVIMIENTO=NOMBRE_PRODUCTO, CANTIDAD_PRODUCTO_MOVIMIENTO=CANTIDAD_PRODUCTO, CODIGO_CABECERA=%s, FECHA_MOVIMIENTO=%s) values(%s,%s)"
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

    def actualizacion(self, datos):
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