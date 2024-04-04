from tkinter import *
from tkinter import messagebox
import sqlite3

root=Tk()

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
ayudaBarra.add_command(label="Licencia")
ayudaBarra.add_command(label="Acerca de...")