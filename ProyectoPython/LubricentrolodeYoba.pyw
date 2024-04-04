from msilib.schema import ComboBox
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3
from tkinter import filedialog
from tkinter.ttk import Style




root=Tk()

root.title("LubricentrolodeYoba")

#Asi se inmobiliza la ventana del programa
# root.resizable(1,0) o ej root.resizable(true,false)

#Asi se modifica la magnitud de la ventana del programa
# root.geometry

#root.iconbitmap("LUBRI.ico")

root.config(bg="black")

#foto=PhotoImage("lubri.jpeg")
#Label(root, image=foto).pack()

    #----------------------------Tablas----------------------------------------------------
tablaMarca=["Frame", "Peugeot", "Renault", "Ford", "Chevrolet"]

tablaTipoProducto=["FiltrodeAceite","FiltrodeAire","Escobillas","Aceite"]


    #-----------------Comienzo de Funciones----------------------------------------------------

    #def abrirUbicacion():

    #    ubiBBDD=filedialog.asksaveasfile(title="Guardar Base de Datos", initialdir="C:", filetypes=(("Ficheros de texto", "*.txt"),("Todos los ficheros","*.*")))

def conexionBBDD():

        miConexion=sqlite3.connect("Productos")

        miCursor=miConexion.cursor()
        
        try:
            miCursor.execute('''
            CREATE TABLE DATAPRODUCTOS (
            CODIGO VARCHAR (10) PRIMARY KEY UNIQUE, 
            MARCA VARCHAR(20), 
            TIPO VARCHAR(20), 
            PRECIO INTEGER(12),
            STOCK INTEGER(100))
            ''')
            messagebox.showinfo("BBDD", "Base de Datos creada con exito")
        except:

            messagebox.showwarning("!Atencion!", "La BBDD ya existe")

def salirAplicacion():

        valor=messagebox.askquestion("Salir", "Desea salir de la aplicacion?")

        if valor=="yes":
            root.destroy()

def limpiarCampos():
        miCodigo.set("")
        miMarca.set("")
        miTipo.set("")
        miPrecio.set("")
        miStock.set("")
        #//textocomentario.delete(1,0, END)//asi se limpia el campo de un cuadro de texto//

def crearDatos():

        miConexion=sqlite3.connect("Productos")

        miCursor=miConexion.cursor()

        datos=miCodigo.get(),  miMarca.get(), miTipo.get(), miPrecio.get(), miStock.get()

        miCursor.execute("INSERT INTO DATAPRODUCTOS VALUES(?,?,?,?,?)",datos)

        miConexion.commit()

        messagebox.showinfo("BBDD", "Producto Guardado con exito")

        """miCursor.execute("INSERT INTO DATAPRODUCTOS VALUES('"miCodigo.get() + 
            "','" + cuadroMarca.get() +
            "','" + miTipo.get("") +
            "','" + miPrecio.get() +  
    #       "','" + textoComentario.get(1.0, END) +         //Asi se agrega dato de tabla tipo TEXTO a diferencia de un tipo ENTRY//      
            "','" + miStock.get() + "')") """
        

def leerDatos():

        miConexion=sqlite3.connect("Productos")

        miCursor=miConexion.cursor()

        miCursor.execute("SELECT * FROM DATAPRODUCTOS WHERE CODIGO=" +miCodigo.get())
        
        elProducto=miCursor.fetchall()

        for producto in elProducto:
            miCodigo.set(producto[0])
            miMarca.set(producto[1])
            miTipo.set(producto[2])
            miPrecio.set(producto[3])
            miStock.set(producto[4])
        miConexion.commit()

        

def actualizarDatos():
        miConexion=sqlite3.connect("Productos")

        miCursor=miConexion.cursor()

        miCursor.execute("UPDATE DATAPRODUCTOS SET MARCA='" + cuadroMarca.get() +
            "', TIPO='" + miTipo.get() +
            "', PRECIO='" + miPrecio.get() +       
            "', STOCK='" + miStock.get() + "'WHERE CODIGO=" + miCodigo.get()) 
        
        miConexion.commit()
        
        messagebox.showinfo("BBDD", "Producto Guardado con exito")

def eliminar():

        miConexion=sqlite3.connect("Productos")

        miCursor=miConexion.cursor()

        valor=messagebox.askquestion("Borrar Producto", "Desea eliminar el producto de forma definitiva?")

        if valor=="yes":
            miCursor.execute("DELETE FROM Tabla WHERE CODIGO=" + miCodigo.get())
            messagebox.showinfo("Borrar Producto","Se ha eliminado el Producto")

        miConexion.commit()

def comprarStock():

        print()

'''stockFinal=miStock.get+1  

        miConexion=sqlite3.connect("Productos")

        miCursor=miConexion.cursor()

        miCursor.execute("UPDATE DATAPRODUCTOS SET STOCK='stockFinal.get()'WHERE CODIGO=" + miCodigo.get()) 
        
        miConexion.commit()
        
        messagebox.showinfo("BBDD", "Producto Vendido")'''
def Historial():

        miConexion=sqlite3.connect("Productos")

        miCursor=miConexion.cursor()

        miCursor.execute("SELECT * FROM DATAPRODUCTOS WHERE CODIGO=" +miCodigo.get())

        
        pass
def Licencias():
       messagebox.showinfo("Licencia","Sofware creado por el tecnico Maldonado Misael")
        


    #--------------Configuracion particular de menu--------------------------------------------

barraMenu=Menu(root, bg="black")
root.config(menu=barraMenu, width=300, height=300)


BasedeDatos=Menu(barraMenu, tearoff=0)
BasedeDatos.add_command(label="Conectar", command=conexionBBDD)
BasedeDatos.add_command(label="Guardar Como")
BasedeDatos.add_separator()
BasedeDatos.add_command(label="Salir", command=salirAplicacion)

admin=Menu(barraMenu, tearoff=0)
admin.add_command(label="Modo Administrador"""", command=fr""")

historial=Menu(barraMenu, tearoff=0)
historial.add_command(label="Historial de Busqueda")
historial.add_command(label="Historial de Chequeado")

ayudaBarra=Menu(barraMenu, tearoff=0) 
ayudaBarra.add_command(label="Licencia", command=Licencias)
ayudaBarra.add_command(label="Acerca de...")

    #Definicion de "botonesopcionales"

barraMenu.add_cascade(label="Base de DD", menu=BasedeDatos)

barraMenu.add_cascade(label="Historial", menu=historial)

barraMenu.add_cascade(label="Ayuda", menu=ayudaBarra)

    #----------------Entrys--------------------------------

miFrame=Frame(root)
miFrame.pack(fill="y", expand="True")
miFrame.config(bg="#D00000", bd="5", relief="groove")

miCodigo=StringVar()
miStock=StringVar()
miTipo=StringVar()
miPrecio=StringVar()
miMarca=StringVar()

"""CuadroFoto=Frame(root2)
    CuadroDescripcion=Frame(root2)
    CuadroHistorial=Frame(root2)
    """

cuadroCodigo=Entry(miFrame, textvariable=miCodigo)
cuadroCodigo.grid(row=0, column=1, padx=10, pady=10)
cuadroCodigo.config(justify="center")


cuadroMarca=ttk.Combobox(miFrame,values=tablaMarca ,state="readonly", textvariable=miMarca) #postcommand=""
cuadroMarca.grid(row=1, column=1, padx=10, pady=10)
cuadroMarca.config(justify="center")

cuadroTipo=ttk.Combobox(miFrame, values=tablaTipoProducto,state="readonly", textvariable=miTipo)
cuadroTipo.grid(row=2, column=1, padx=10, pady=10)
cuadroTipo.config(justify="center")


cuadroPrecio=Entry(miFrame, textvariable=miPrecio)
cuadroPrecio.grid(row=3, column=1, padx=10, pady=10)

cuadroStock=Entry(miFrame, textvariable=miStock)
cuadroStock.grid(row=4, column=1, padx=10, pady=10)
cuadroStock.config(justify="center")

#------------Comienzan las Etiquetas(labels)---------------------------

idLabel=Label(miFrame, text="Codigo")
idLabel.grid(row=0, column=0, sticky="e", padx=10, pady=10)
idLabel.config(bg="black", state="disabled", disabledforeground="white", font=("Arial", "15"))

marcaLabel=Label(miFrame, text="Marca")
marcaLabel.grid(row=1, column=0, sticky="e", padx=10, pady=10)
marcaLabel.config(bg="black", state="disabled", disabledforeground="white", font=("Arial", "15"))

modeloLabel=Label(miFrame, text="Tipo de Producto")
modeloLabel.grid(row=2, column=0, sticky="e", padx=10, pady=10)
modeloLabel.config(bg="black", state="disabled", disabledforeground="white", font=("Arial", "15"))

tipoLabel=Label(miFrame, text="Precio   ")
tipoLabel.grid(row=3, column=0, sticky="e", padx=10, pady=10)
tipoLabel.config(bg="black", state="disabled", disabledforeground="white", font=("Arial", "15"))

precioLabel=Label(miFrame, text="Stock")
precioLabel.grid(row=4, column=0, sticky="e", padx=10, pady=10)
precioLabel.config(bg="black", state="disabled", disabledforeground="white", font=("Arial", "15"))

precioLabel2=Label(miFrame, text="$")
precioLabel2.grid(row=3, column=0, sticky="e", padx=10, pady=10)
precioLabel2.config(bg="white", state="disabled", disabledforeground="black", justify="left", font=("Arial", "15"))

#----------------Comienzo de Botones Vender y Comprar--------------------------
"""
botonComprar=Button(miFrame, text="Comprar", command=comprarStock)
botonComprar.grid(row=5, column=0, sticky="e", padx=1, pady=1)
botonComprar.config(bg="black", bd="5", cursor="hand2", relief="raised", foreground="white", activebackground="#C20808", font=("Arial Black", "10"))

botonVender=Button(miFrame, text="Vender", command=limpiarCampos)
botonVender.grid(row=5, column=1, sticky="e", padx=1, pady=1)
botonVender.config(bg="black", bd="5", cursor="hand2", relief="raised", foreground="white", activebackground="#C20808", font=("Arial Black", "10"), justify="left")
"""
#----------------Comienzo de Botones Inntermedios--------------------------

miFrame3=Frame(root, bg="#D00000", bd="5", relief="groove")
miFrame3.pack()


botonLeer=Button(miFrame3, text="BUSCAR", command=leerDatos)
botonLeer.grid(row=0, column=2 , sticky="e", padx=10, pady=10)
botonLeer.config(bg="white", bd="5", cursor="hand2", relief="raised", foreground="black", activebackground="#C20808", font=("Arial Black", "10"))

botonActualizar=Button(miFrame3, text="ACTUALIZAR" , command=actualizarDatos)
botonActualizar.grid(row=0, column=1, sticky="e", padx=10, pady=10)
botonActualizar.config(bg="white", bd="5", cursor="exchange", relief="raised", foreground="black", activebackground="#C20808", font=("Arial Black", "10"))

#----------------Comienzo de Botones Inferiores--------------------------


miFrame2=Frame(root)
miFrame2.pack()
miFrame2.config(bg="#D00000", bd="5", relief="groove")

botonCrear=Button(miFrame2, text="CREAR", command=crearDatos)
botonCrear.grid(row=1, column=0, sticky="e", padx=10, pady=10)
botonCrear.config(bg="black", bd="3", cursor="hand2", relief="raised", foreground="white", activebackground="#C20808", font=("Arial Black", "10"))


botonBorrar=Button(miFrame2, text="BORRAR", command=eliminar)
botonBorrar.grid(row=1, column=2, sticky="e", padx=10, pady=10)
botonBorrar.config(bg="black", bd="3", cursor="pirate", relief="raised", foreground="white", activebackground="#C20808", font=("Arial Black", "10"))

botonLimpiar=Button(miFrame2, text="LIMPIAR CASILLAS", command=limpiarCampos)
botonLimpiar.grid(row=1, column=3, sticky="e", padx=10, pady=10)
botonLimpiar.config(bg="black", bd="8", cursor="hand2", relief="raised", foreground="white", activebackground="#C20808", font=("Arial Black", "10"))

#--------------------PantaLLA-----------------------------



root.mainloop()