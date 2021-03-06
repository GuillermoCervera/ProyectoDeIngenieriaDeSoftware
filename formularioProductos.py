# Guillermo Cervera

from tkinter import *
import tkinter.messagebox
import mysql.connector

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
from tkinter import scrolledtext as st
import datosProductos

connectiondb = mysql.connector.connect(host="localhost", user="root", passwd="", database="DISTRIBUIDOR")
cursordb = connectiondb.cursor()

def login():
    global root2
    root2 = Toplevel(root)
    root2.title("Iniciar sesión")
    root2.geometry("450x300")

    global username_verification
    global password_verification
    Label(root2, text='Por favor, introduzca sus datos.', font=('arial', 12, 'bold'), fg="blue", width=300).pack()
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
            self.producto1=datosProductos.Productos()
            self.ventana1=tk.Tk()
            self.ventana1.title("Distribuidor de bebidas azucaradas")
            self.ventana1.geometry("600x500")
            self.cuaderno1=ttk.Notebook(self.ventana1)        
            self.alta_productos()
            self.listado_completo()
            self.modificar()
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
            self.entrynombre.grid(column=0, row=1, padx=4, pady=4)
            self.label2=ttk.Label(self.labelframe1, text="Cantidad:")        
            self.label2.grid(column=0, row=2, padx=4, pady=4)
            self.cantidadalta=tk.StringVar()
            self.entrycantidad=ttk.Entry(self.labelframe1, textvariable=self.cantidadalta)
            self.entrycantidad.grid(column=0, row=3, padx=4, pady=4)
            self.boton1=ttk.Button(self.labelframe1, text="Dar de alta", command=self.agregar)
            self.boton1.grid(column=0, row=4, padx=4, pady=4)

        def agregar(self):
            datos=(self.nombrealta.get(), self.cantidadalta.get())
            self.producto1.alta(datos)
            mb.showinfo("Información", "El producto fue dado de alta")
            self.nombrealta.set("")
            self.cantidadalta.set("")

        def listado_completo(self):
                self.pagina3=ttk.Frame(self.cuaderno1)
                self.cuaderno1.add(self.pagina3, text="Consultar productos")
                self.labelframe3=ttk.LabelFrame(self.pagina3, text="Consulta de productos")
                self.labelframe3.grid(column=0, row=1, padx=5, pady=10)
                self.scrolledtext1=st.ScrolledText(self.labelframe3, width=20, height=3)
                self.scrolledtext1.grid(column=0, row=0, padx=4, pady=4)
                self.boton1=ttk.Button(self.labelframe3, text="Listar todos los productos", command=self.listar)
                self.boton1.grid(column=0, row=1, padx=4, pady=4)
                self.label1=ttk.Label(self.labelframe3, text="")
                self.label1.grid(column=0, row=2, padx=4, pady=4)
                self.label1=ttk.Label(self.labelframe3, text="Código:")
                self.label1.grid(column=0, row=3, padx=1, pady=1)
                self.codigolist=tk.StringVar()
                self.entrycodigolist=ttk.Entry(self.labelframe3, textvariable=self.codigolist, state="readonly")
                self.entrycodigolist.grid(column=0, row=4, padx=1, pady=1)
                self.label2=ttk.Label(self.labelframe3, text="Nombre:")
                self.label2.grid(column=0, row=5, padx=1, pady=1)
                self.nombrelist=tk.StringVar()
                self.entrynombrelist=ttk.Entry(self.labelframe3, textvariable=self.nombrelist)
                self.entrynombrelist.grid(column=0, row=6, padx=1, pady=1)
                self.label3=ttk.Label(self.labelframe3, text="Cantidad:")        
                self.label3.grid(column=0, row=7, padx=1, pady=1)
                self.cantidadlist=tk.StringVar()
                self.entrycantidadlist=ttk.Entry(self.labelframe3, textvariable=self.cantidadlist, state="readonly")
                self.entrycantidadlist.grid(column=0, row=8, padx=4, pady=4)
                self.boton1=ttk.Button(self.labelframe3, text="Consultar", command=self.consultar_listar)
                self.boton1.grid(column=0, row=9, padx=4, pady=4)

        def listar(self):
            respuesta=self.producto1.lista_todos()
            self.scrolledtext1.delete("1.0", tk.END)        
            for fila in respuesta:
                self.scrolledtext1.insert(tk.END, "Código: "+str(fila[0])+
                                              "\nNombre: "+fila[1]+
                                              "\nCantidad: "+str(fila[2])+"\n\n")

        def consultar_listar(self):
            datos=(self.nombrelist.get(), )
            respuesta=self.producto1.consulta(datos)
            if len(respuesta)>0:
                #self.codigolist.set(respuesta[0][0])
                self.nombrelist.set(respuesta[0][1])
                self.cantidadlist.set(respuesta[0][2])
            else:
                #self.codigolist.set('')
                self.nombrelist.set('')
                self.cantidadlist.set('')
                mb.showinfo("Información", "No existe ningún producto con el nombre introducido")

        def consultar_act(self):
            datos=(self.nombreact.get(), )
            respuesta=self.producto1.consulta(datos)
            if len(respuesta)>0:
                self.codigoact.set(respuesta[0][0])
                self.nombreact.set(respuesta[0][1])
                self.cantidadact.set(respuesta[0][2])
            else:
                self.codigoact.set('')
                self.nombreact.set('')
                self.cantidadact.set('')
                mb.showinfo("Información", "No existe ningún producto como el consultado")

        def modificar(self):
            self.pagina5=ttk.Frame(self.cuaderno1)
            self.cuaderno1.add(self.pagina5, text="Modificar producto")
            self.labelframe5=ttk.LabelFrame(self.pagina5, text="Modificación de productos")
            self.labelframe5.grid(column=0, row=0, padx=5, pady=10)
            #self.label1=ttk.Label(self.labelframe5, text="Código:")
            #self.label1.grid(column=0, row=0, padx=4, pady=4)
            self.codigoact=tk.StringVar()
            #self.entrycodigo=ttk.Entry(self.labelframe5, textvariable=self.codigoact, state="readonly")
            #self.entrycodigo.grid(column=1, row=0, padx=4, pady=4)
            self.label2=ttk.Label(self.labelframe5, text="Nombre:")
            self.label2.grid(column=0, row=1, padx=4, pady=4)
            self.nombreact=tk.StringVar()
            self.entrynombre=ttk.Entry(self.labelframe5, textvariable=self.nombreact)
            self.entrynombre.grid(column=0, row=2, padx=4, pady=4)
            self.label3=ttk.Label(self.labelframe5, text="Cantidad:")        
            self.label3.grid(column=0, row=3, padx=4, pady=4)
            self.cantidadact=tk.StringVar()
            self.entrycantidad=ttk.Entry(self.labelframe5, textvariable=self.cantidadact)
            self.entrycantidad.grid(column=0, row=4, padx=4, pady=4)
            self.label2=ttk.Label(self.labelframe5, text="Motivo:")
            self.label2.grid(column=0, row=5, padx=4, pady=4)
            self.motivoact=tk.StringVar()
            self.entrymotivo=ttk.Entry(self.labelframe5, textvariable=self.motivoact)
            self.entrymotivo.grid(column=0, row=6, padx=4, pady=4)
            self.boton1=ttk.Button(self.labelframe5, text="Consultar", command=self.consultar_act)
            self.boton1.grid(column=0, row=7, padx=4, pady=4)
            self.boton1=ttk.Button(self.labelframe5, text="Modificar", command=self.modifica)
            self.boton1.grid(column=0, row=8, padx=4, pady=4)

        def modifica(self):
            datos=(self.nombreact.get(), self.cantidadact.get(), self.codigoact.get())
            numero=self.producto1.modificacion(datos)
            if numero==1:
                mb.showinfo("Información", "Se modificó el producto")
            else:
                mb.showinfo("Información", "No existe ningún producto como el consultado")

        def borrado(self):
            self.pagina4=ttk.Frame(self.cuaderno1)
            self.cuaderno1.add(self.pagina4, text="Dar de baja productos")
            self.labelframe4=ttk.LabelFrame(self.pagina4, text="Baja de productos")        
            self.labelframe4.grid(column=0, row=0, padx=5, pady=10)
            self.label1=ttk.Label(self.labelframe4, text="Nombre:")
            self.label1.grid(column=0, row=1, padx=4, pady=4)
            self.nombreborra=tk.StringVar()
            self.entryborra=ttk.Entry(self.labelframe4, textvariable=self.nombreborra)
            self.entryborra.grid(column=0, row=2, padx=4, pady=4)
            self.boton1=ttk.Button(self.labelframe4, text="Dar de baja", command=self.borrar)
            self.boton1.grid(column=0, row=3, padx=4, pady=4)

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