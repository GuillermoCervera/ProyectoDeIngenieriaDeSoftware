import mysql.connector

class Productos:

    def abrir(self):
        conexion=mysql.connector.connect(host="localhost", 
                                              user="root", 
                                              passwd="", 
                                              database="distribuidor")
        return conexion

    def alta(self, datos):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="insert into productos(nombre, cantidad) values (%s,%s)"
        cursor.execute(sql, datos)
        cone.commit()
        cone.close()

    def actualizacion(self, datos):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="update productos set nombre=%s, cantidad=%s where id=%s"
        cursor.execute(sql, datos)
        cone.commit()
        cone.close()
        return cursor.rowcount

    def baja(self, datos):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="delete from productos where id=%s"
        cursor.execute(sql, datos)
        cone.commit()
        cone.close()
        return cursor.rowcount