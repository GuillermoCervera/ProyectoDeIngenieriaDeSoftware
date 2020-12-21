#Guillermo Cervera

from tkinter import *
import tkinter.messagebox
import mysql.connector

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
from tkinter import scrolledtext as st
import productos

connectiondb = mysql.connector.connect(host="localhost", user="root", passwd="", database="DISTRIBUIDOR")
cursordb = connectiondb.cursor()

def login():
    global root2
    root2 = Toplevel(root)
    root2.title("Iniciar sesión")
    root2.geometry("450x300")

    global username_verification
    global password_verification
    Label(root2, text='Por favor, introduzca sus datos.', font=('arial', 12, 'bold'), fg="black", width=300).pack()
    username_verification = StringVar()
    password_verification = StringVar()
    Label(root2, text="").pack()
    Label(root2, text="Usuario:", fg="black", font=('arial', 12, 'bold')).pack()
    Entry(root2, textvariable=username_verification).pack()
    Label(root2, text="").pack()
    Label(root2, text="Contraseña:", fg="black", font=('arial', 12, 'bold')).pack()
    Entry(root2, textvariable=password_verification, show="*").pack()
    Label(root2, text="").pack()
    Button(root2, text="Acceder", fg='black', font=('arial', 12, 'bold'), command=login_verification).pack()
    Label(root2, text="")

def logged_destroy():
    logged_message.destroy()
    root2.destroy()

def failed_destroy():
    failed_message.destroy()

def logged():
    class FormularioProductos:
        root2.destroy()
        Exit()

        def __init__(self):
            self.producto1=productos.Productos()
            self.ventana1=tk.Tk()
            self.ventana1.title("Distribuidor de bebidas azucaradas")
            self.ventana1.geometry("600x500")
            self.cuaderno1=ttk.Notebook(self.ventana1)        
            self.alta_productos()
            self.listado_completo()
            self.consulta()
            self.actualizar()
            self.borrado()
            self.cuaderno1.grid(column=0, row=0, padx=10, pady=10)
            self.ventana1.mainloop()
            root.destroy()

        def alta_productos(self):
            self.pagina1=ttk.Frame(self.cuaderno1)
            self.cuaderno1.add(self.pagina1, text="Dar de alta productos")
            self.labelframe1=ttk.LabelFrame(self.pagina1, text="Alta de productos")        
            self.labelframe1.grid(column=0, row=0, padx=5, pady=10)
            self.label1=ttk.Label(self.labelframe1, text="Nombre:")
            self.label1.grid(column=0, row=0, padx=4, pady=4)
            self.nombrealta=tk.StringVar()
            self.entrynombre=ttk.Entry(self.labelframe1, textvariable=self.nombrealta)
            self.entrynombre.grid(column=1, row=0, padx=4, pady=4)
            self.label2=ttk.Label(self.labelframe1, text="Cantidad:")        
            self.label2.grid(column=0, row=1, padx=4, pady=4)
            self.cantidadalta=tk.StringVar()
            self.entrycantidad=ttk.Entry(self.labelframe1, textvariable=self.cantidadalta)
            self.entrycantidad.grid(column=1, row=1, padx=4, pady=4)
            #self.label1=ttk.Label(self.labelframe1, text="Cabecera:")
            #self.label1.grid(column=0, row=2, padx=4, pady=4)
            #self.codigocabecera=tk.StringVar()
            #self.entrycabecera=ttk.Entry(self.labelframe1, textvariable=self.codigocabecera)
            #self.entrycabecera.grid(column=1, row=2, padx=4, pady=4)
            #self.label1=ttk.Label(self.labelframe1, text="Fecha:")
            #self.label1.grid(column=0, row=3, padx=4, pady=4)
            #self.fechamovimiento=tk.StringVar()
            #self.entryfecha=ttk.Entry(self.labelframe1, textvariable=self.fechamovimiento)
            #self.entryfecha.grid(column=1, row=3, padx=4, pady=4)
            self.boton1=ttk.Button(self.labelframe1, text="Dar de alta", command=self.agregar)
            self.boton1.grid(column=1, row=4, padx=4, pady=4)

        def agregar(self):
            datos=(self.nombrealta.get(), self.cantidadalta.get())
            #datos=(self.nombrealta.get(), self.cantidadalta.get(), self.codigocabecera.get(), self.fechamovimiento.get())
            self.producto1.alta(datos)
            mb.showinfo("Información", "El producto fue dado de alta")
            self.nombrealta.set("")
            self.cantidadalta.set("")
            #self.codigocabecera.set("")
            #self.fechamovimiento.set("")

        def listado_completo(self):
            self.pagina3=ttk.Frame(self.cuaderno1)
            self.cuaderno1.add(self.pagina3, text="Listar productos")
            self.labelframe3=ttk.LabelFrame(self.pagina3, text="Listado de todos los productos")
            self.labelframe3.grid(column=0, row=0, padx=5, pady=10)
            self.boton1=ttk.Button(self.labelframe3, text="Listar", command=self.listar)
            self.boton1.grid(column=0, row=0, padx=4, pady=4)
            self.boton1=ttk.Button(self.labelframe3, text="Descargar reporte")
            self.boton1.grid(column=1, row=1, padx=4, pady=4)
            self.scrolledtext1=st.ScrolledText(self.labelframe3, width=40, height=20)
            self.scrolledtext1.grid(column=0,row=1, padx=10, pady=10)

        def listar(self):
            respuesta=self.producto1.lista_todos()
            self.scrolledtext1.delete("1.0", tk.END)        
            for fila in respuesta:
                self.scrolledtext1.insert(tk.END, "Código: "+str(fila[0])+
                                                "\nNombre: "+fila[1]+
                                                "\nCantidad: "+str(fila[2])+"\n\n")

        def consulta(self):
            self.pagina2=ttk.Frame(self.cuaderno1)
            self.cuaderno1.add(self.pagina2, text="Consultar productos")
            self.labelframe2=ttk.LabelFrame(self.pagina2, text="Consulta de productos")
            self.labelframe2.grid(column=0, row=0, padx=5, pady=10)
            self.label1=ttk.Label(self.labelframe2, text="Código:")
            self.label1.grid(column=0, row=0, padx=4, pady=4)
            self.CODIGO_PRODUCTO=tk.StringVar()
            self.entryCODIGO_PRODUCTO=ttk.Entry(self.labelframe2, textvariable=self.CODIGO_PRODUCTO, state="readonly")
            self.entryCODIGO_PRODUCTO.grid(column=1, row=0, padx=4, pady=4)
            self.label2=ttk.Label(self.labelframe2, text="Nombre:")        
            self.label2.grid(column=0, row=1, padx=4, pady=4)
            self.NOMBRE_PRODUCTO=tk.StringVar()
            self.entryNOMBRE_PRODUCTO=ttk.Entry(self.labelframe2, textvariable=self.NOMBRE_PRODUCTO)
            self.entryNOMBRE_PRODUCTO.grid(column=1, row=1, padx=4, pady=4)
            self.label3=ttk.Label(self.labelframe2, text="Cantidad:")        
            self.label3.grid(column=0, row=2, padx=4, pady=4)
            self.CANTIDAD_PRODUCTO=tk.StringVar()
            self.entryCANTIDAD_PRODUCTO=ttk.Entry(self.labelframe2, textvariable=self.CANTIDAD_PRODUCTO, state="readonly")
            self.entryCANTIDAD_PRODUCTO.grid(column=1, row=2, padx=4, pady=4)
            self.boton1=ttk.Button(self.labelframe2, text="Consultar", command=self.consultar)
            self.boton1.grid(column=1, row=3, padx=4, pady=4)

        def consultar(self):
            datos=(self.NOMBRE_PRODUCTO.get(), )
            respuesta=self.producto1.consulta(datos)
            if len(respuesta)>0:
                self.CODIGO_PRODUCTO.set(respuesta[0][0])
                self.NOMBRE_PRODUCTO.set(respuesta[0][1])
                self.CANTIDAD_PRODUCTO.set(respuesta[0][2])
            else:
                self.CODIGO_PRODUCTO.set('')
                self.NOMBRE_PRODUCTO.set('')
                self.CANTIDAD_PRODUCTO.set('')
                mb.showinfo("Información", "No existe ningún producto con el nombre introducido")

        def actualizar(self):
            self.pagina5=ttk.Frame(self.cuaderno1)
            self.cuaderno1.add(self.pagina5, text="Actualizar productos")
            self.labelframe5=ttk.LabelFrame(self.pagina5, text="Actualización de productos")
            self.labelframe5.grid(column=0, row=0, padx=5, pady=10)
            self.label1=ttk.Label(self.labelframe5, text="Código:")
            self.label1.grid(column=0, row=0, padx=4, pady=4)
            self.idact=tk.StringVar()
            self.entryid=ttk.Entry(self.labelframe5, textvariable=self.idact)
            self.entryid.grid(column=1, row=0, padx=4, pady=4)
            self.label2=ttk.Label(self.labelframe5, text="Nombre:")        
            self.label2.grid(column=0, row=1, padx=4, pady=4)
            self.nombreact=tk.StringVar()
            self.entrynombre=ttk.Entry(self.labelframe5, textvariable=self.nombreact)
            self.entrynombre.grid(column=1, row=1, padx=4, pady=4)
            self.label3=ttk.Label(self.labelframe5, text="Cantidad:")        
            self.label3.grid(column=0, row=2, padx=4, pady=4)
            self.cantidadact=tk.StringVar()
            self.entrycantidad=ttk.Entry(self.labelframe5, textvariable=self.cantidadact)
            self.entrycantidad.grid(column=1, row=2, padx=4, pady=4)
            self.boton1=ttk.Button(self.labelframe5, text="Actualizar", command=self.actualiza)
            self.boton1.grid(column=1, row=4, padx=4, pady=4)

        def actualiza(self):
            datos=(self.nombreact.get(), self.cantidadact.get(), self.idact.get())
            numero=self.producto1.actualizacion(datos)
            if numero==1:
                mb.showinfo("Información", "Se actualizó el producto")
            else:
                mb.showinfo("Información", "No existe ningún producto con dicho código")

        def borrado(self):
            self.pagina4=ttk.Frame(self.cuaderno1)
            self.cuaderno1.add(self.pagina4, text="Dar de baja productos")
            self.labelframe4=ttk.LabelFrame(self.pagina4, text="Baja de productos")        
            self.labelframe4.grid(column=0, row=0, padx=5, pady=10)
            self.label1=ttk.Label(self.labelframe4, text="Nombre:")
            self.label1.grid(column=0, row=0, padx=4, pady=4)
            self.nombreborra=tk.StringVar()
            self.entryborra=ttk.Entry(self.labelframe4, textvariable=self.nombreborra)
            self.entryborra.grid(column=1, row=0, padx=4, pady=4)
            self.boton1=ttk.Button(self.labelframe4, text="Dar de baja", command=self.borrar)
            self.boton1.grid(column=1, row=1, padx=4, pady=4)

        def borrar(self):
            datos=(self.nombreborra.get(), )
            numero=self.producto1.baja(datos)
            if numero==1:
                mb.showinfo("Información", "Se dio de baja el producto introducido")
            else:
                mb.showinfo("Información", "No existe ningún producto con el nombre introducido")

    aplicacion1=FormularioProductos()

def failed():
    global failed_message
    failed_message = Toplevel(root2)
    failed_message.title("Usuario o contraseña incorrecto")
    failed_message.geometry("500x100")
    Label(failed_message, text="El usuario o la contraseña no son correctos", fg="red", font="bold").pack()
    Label(failed_message, text="").pack()
    Button(failed_message,text="Volver", fg='black', font=('arial', 12, 'bold'), command=failed_destroy).pack()

def login_verification():
    user_verification = username_verification.get()
    pass_verification = password_verification.get()
    sql = "select * from usuario where NOMBRE_USUARIO = %s and CONTRASEÑA_USUARIO = %s"
    cursordb.execute(sql,[(user_verification),(pass_verification)])
    results = cursordb.fetchall()
    if results:
        for i in results:
            logged()
            break
    else:
        failed()

def Exit():
    root.destroy()

def main_display():
    global root
    root = Tk()
    #root.config(bg="lightgray")
    root.title("Login")
    root.geometry("500x500")
    Label(root,text='Distribuidor de bebidas azucaradas', font=('arial', 20, 'bold'), fg="blue", width=300).pack()
    Label(root,text="").pack()
    Button(root, text='Identificarse', height="1", width="20", font=('arial', 12, 'bold'), fg="black", command=login).pack()
    Label(root,text="").pack()
    Button(root, text='Salir', height="1", width="20", font=('arial', 12, 'bold'), fg="black", command=Exit).pack()
    Label(root,text="").pack()

main_display()
root.mainloop()