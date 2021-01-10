# Guillermo Cervera

import io
import xlwt
import pymysql
from flask import Flask, Response, render_template
from flaskext.mysql import MySQL

app = Flask(__name__)

mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'DISTRIBUIDOR'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

@app.route('/')
def upload_form():
    return render_template('download.html')

@app.route('/download/report/excel')
def download_report():
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        
        cursor.execute("SELECT codigo_producto, nombre_producto, cantidad_producto FROM producto")
        result = cursor.fetchall()
        
        # Output en bytes
        output = io.BytesIO()
        
        # Crear objeto WorkBook
        workbook = xlwt.Workbook()
        
        # Añadir hoja
        sh = workbook.add_sheet('Reporte productos')
        
        sh.write(0, 0, 'Distribuidor de bebidas azucaradas')
        sh.write(1, 0, 'Dirección: Avenida Constitución, 1')
        sh.write(2, 0, 'Código Postal: 46000')
        sh.write(3, 0, 'Teléfono: 123456789')
        sh.write(4, 0, 'Email: distribuidor@email.com')

        sh.write(6, 0, 'Atendido por: Guillermo Cervera')
        sh.write(7, 0, 'Fecha: 10/01/2021')
        sh.write(8, 0, 'Factura: 1')

        # Cabecera
        sh.write(10, 0, 'CÓDIGO PRODUCTO')
        sh.write(10, 1, 'NOMBRE PRODUCTO')
        sh.write(10, 2, 'CANTIDAD PRODUCTO')
        
        idx = 0
        for row in result:
            sh.write(idx+11, 0, str(row['codigo_producto']))
            sh.write(idx+11, 1, str(row['nombre_producto']))
            sh.write(idx+11, 2, str(row['cantidad_producto']))
            idx += 1
        
        workbook.save(output)
        output.seek(0)
        
        return Response(output, mimetype="application/ms-excel", headers={"Content-Disposition":"attachment;filename=Reporte_productos.xls"})
    except Exception as e:
        print(e)
    finally:
        cursor.close() 
        conn.close()

if __name__ == "__main__":
    app.run()