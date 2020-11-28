import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
from tkinter import scrolledtext as st
import productos

class FormularioProductos:
    def __init__(self):
        self.producto1=productos.Productos()
        self.ventana1=tk.Tk()
        self.ventana1.title("Distribuidor de productos azucarados")
        self.cuaderno1=ttk.Notebook(self.ventana1)        
        self.alta_productos()
        self.listado_completo()
        #self.consulta_por_id()
        self.actualizar()
        self.borrado()
        self.cuaderno1.grid(column=0, row=0, padx=10, pady=10)
        self.ventana1.mainloop()

    def alta_productos(self):
        self.pagina1=ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina1, text="Dar de alta producto")
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
        self.boton1=ttk.Button(self.labelframe1, text="Dar de alta", command=self.agregar)
        self.boton1.grid(column=1, row=2, padx=4, pady=4)

    def agregar(self):
        datos=(self.nombrealta.get(), self.cantidadalta.get())
        self.producto1.alta(datos)
        mb.showinfo("Información", "El producto fue dado de alta")
        self.nombrealta.set("")
        self.cantidadalta.set("")

    def listado_completo(self):
        self.pagina3=ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina3, text="Listar productos")
        self.labelframe3=ttk.LabelFrame(self.pagina3, text="Lista de productos")
        self.labelframe3.grid(column=0, row=0, padx=5, pady=10)
        self.boton1=ttk.Button(self.labelframe3, text="Listar todos los productos", command=self.listar)
        self.boton1.grid(column=0, row=0, padx=4, pady=4)
        self.scrolledtext1=st.ScrolledText(self.labelframe3, width=40, height=20)
        self.scrolledtext1.grid(column=0,row=1, padx=10, pady=10)

    def listar(self):
        respuesta=self.producto1.recuperar_todos()
        self.scrolledtext1.delete("1.0", tk.END)        
        for fila in respuesta:
            self.scrolledtext1.insert(tk.END, "ID: "+str(fila[0])+
                                              "\nNombre: "+fila[1]+
                                              "\nCantidad: "+str(fila[2])+"\n\n")

    #def consulta_por_id(self):
        #self.pagina2=ttk.Frame(self.cuaderno1)
        #self.cuaderno1.add(self.pagina2, text="Consultar producto")
        #self.labelframe2=ttk.LabelFrame(self.pagina2, text="Consulta de productos")
        #self.labelframe2.grid(column=0, row=0, padx=5, pady=10)
        #self.label1=ttk.Label(self.labelframe2, text="ID:")
        #self.label1.grid(column=0, row=0, padx=4, pady=4)
        #self.id=tk.StringVar()
        #self.entryid=ttk.Entry(self.labelframe2, textvariable=self.id)
        #self.entryid.grid(column=1, row=0, padx=4, pady=4)
        #self.label2=ttk.Label(self.labelframe2, text="Nombre:")        
        #self.label2.grid(column=0, row=1, padx=4, pady=4)
        #self.nombre=tk.StringVar()
        #self.entrynombre=ttk.Entry(self.labelframe2, textvariable=self.nombre, state="readonly")
        #self.entrynombre.grid(column=1, row=1, padx=4, pady=4)
        #self.label3=ttk.Label(self.labelframe2, text="Cantidad:")        
        #self.label3.grid(column=0, row=2, padx=4, pady=4)
        #self.cantidad=tk.StringVar()
        #self.entrycantidad=ttk.Entry(self.labelframe2, textvariable=self.cantidad, state="readonly")
        #self.entrycantidad.grid(column=1, row=2, padx=4, pady=4)
        #self.boton1=ttk.Button(self.labelframe2, text="Consultar", command=self.consultar)
        #self.boton1.grid(column=1, row=3, padx=4, pady=4)"""

    #def consultar(self):
        #datos=(self.id.get(), )
        #respuesta=self.producto1.consulta(datos)
        #if len(respuesta)>0:
            #self.nombre.set(respuesta[0][0])
            #self.cantidad.set(respuesta[0][1])
        #else:
            #self.nombre.set('')
            #self.cantidad.set('')
            #mb.showinfo("Información", "No existe ningún producto con dicho ID")

    def actualizar(self):
        self.pagina5=ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina5, text="Actualizar producto")
        self.labelframe5=ttk.LabelFrame(self.pagina5, text="Actualización de productos")
        self.labelframe5.grid(column=0, row=0, padx=5, pady=10)
        self.label1=ttk.Label(self.labelframe5, text="ID:")
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
        #self.boton2=ttk.Button(self.labelframe5, text="Consultar", command=self.consultar_act)
        #self.boton2.grid(column=1, row=3, padx=4, pady=4)
        self.boton1=ttk.Button(self.labelframe5, text="Actualizar", command=self.actualiza)
        self.boton1.grid(column=1, row=4, padx=4, pady=4)

    def actualiza(self):
        datos=(self.nombreact.get(), self.cantidadact.get(), self.idact.get())
        numero=self.producto1.actualizacion(datos)
        if numero==1:
            mb.showinfo("Información", "Se actualizó el producto")
        else:
            mb.showinfo("Información", "No existe ningún producto con dicho ID")

    def consultar_act(self):
        datos=(self.idact.get(), )
        respuesta=self.producto1.consulta(datos)
        if len(respuesta)>0:
            self.nombreact.set(respuesta[0][0])
            self.cantidadact.set(respuesta[0][1])
        else:
            self.nombreact.set('')
            self.cantidadact.set('')
            mb.showinfo("Información", "No existe ningún producto con dicho ID")

    def borrado(self):
        self.pagina4=ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina4, text="Dar de baja producto")
        self.labelframe4=ttk.LabelFrame(self.pagina4, text="Baja de productos")        
        self.labelframe4.grid(column=0, row=0, padx=5, pady=10)
        self.label1=ttk.Label(self.labelframe4, text="ID:")
        self.label1.grid(column=0, row=0, padx=4, pady=4)
        self.idborra=tk.StringVar()
        self.entryborra=ttk.Entry(self.labelframe4, textvariable=self.idborra)
        self.entryborra.grid(column=1, row=0, padx=4, pady=4)
        self.boton1=ttk.Button(self.labelframe4, text="Dar de baja", command=self.borrar)
        self.boton1.grid(column=1, row=1, padx=4, pady=4)

    def borrar(self):
        datos=(self.idborra.get(), )
        numero=self.producto1.baja(datos)
        if numero==1:
            mb.showinfo("Información", "Se dio de baja el producto con dicho ID")
        else:
            mb.showinfo("Información", "No existe ningún producto con dicho ID")

aplicacion1=FormularioProductos()