from tkinter import *
from tkinter import ttk
import subprocess
import pandas as pd
from tkinter import messagebox
import datetime

Ingresar_p = Tk()

Ingresar_p.title("Ingresar Producto")
Ingresar_p.resizable(False,False)
Ingresar_p.configure(bg="#1E4024")

#Mide las dimensiones de la pantalla y posiciona la pantalla en el centro
screenwidth = Ingresar_p.winfo_screenwidth()
screenheight = Ingresar_p.winfo_screenheight()

x = (screenwidth/2) - (1000/2)
y = (screenheight/2) - (900/2)

Ingresar_p.geometry("%dx%d+%d+%d" % (1000, 900, x, y))

def volver():
    Ingresar_p.destroy()
    subprocess.call(["python","Code/Menu_principal.py"])

volver_b = Button(
    Ingresar_p,
    text = "Volver",
    command = volver,
    borderwidth=0,
    activebackground="#1E4024",
    activeforeground="#FFFFFF"
)
volver_b.configure(
    font = ("Bahnschrift", 12),
    fg = "#FFFFFF",
    bg = "#1E4024"
)

volver_b.place(x=10, y=10)

#---------------------------------------

#Recuadro para ingresar el nombre del producto
nombre = Label(
    Ingresar_p,
    text = "Nombre del producto",
    font = ("Bahnschrift", 12),
    fg = "#FFFFFF",
    bg = "#1E4024"
)

nombre.place(x = 50,y = 50)


nombre_producto = Entry(
    Ingresar_p
)

nombre_producto.place(x = 50, y = 90)


#------------------------------------

#Recuadro para ingresar la cantidad de producto
cantidad = Label(
    Ingresar_p,
    text = "Cantidad del producto",
    font = ("Bahnschrift", 12),
    fg = "#FFFFFF",
    bg = "#1E4024"
)

cantidad.place(x = 50,y = 130)


cantidad_producto = Entry(
    Ingresar_p
)

cantidad_producto.place(x = 50, y = 170)

#-------------------------------------

#Recuadro para ingresar el costo de producto
costo = Label(
    Ingresar_p,
    text = "Costo del producto",
    font = ("Bahnschrift", 12),
    fg = "#FFFFFF",
    bg = "#1E4024"
)

costo.place(x = 50,y = 210)


costo_producto = Entry(
    Ingresar_p
)

costo_producto.place(x = 50, y = 250)

#-------------------------------------

#Recuadro para ingresar el precio de venta
precio_venta = Label(
    Ingresar_p,
    text = "Precio de venta",
    font = ("Bahnschrift", 12),
    fg = "#FFFFFF",
    bg = "#1E4024"
)

precio_venta.place(x = 50,y = 290)


precio_v = Entry(
    Ingresar_p
)

precio_v.place(x = 50, y = 330)

#-------------------------------------

#Recuadro para ingresar la fecha de vencimiento
fecha_vence = Label(
    Ingresar_p,
    text = "Fecha Vencimiento",
    font = ("Bahnschrift", 12),
    fg = "#FFFFFF",
    bg = "#1E4024"
)

fecha_vence.place(x = 50,y = 370)


fecha_v = Entry(
    Ingresar_p
)

fecha_v.place(x = 50, y = 410)

#-------------------------------------
tabla = ttk.Treeview(
    Ingresar_p
)

#Carga el archivo csv con la libreria pandas(nombrada como pd)
df = pd.read_csv("./Database/productos.csv")

tabla['columns'] = ("ID","Nombre", "Cantidad", "Costo Compra", "Precio Venta","Fecha de vencimiento")

tabla.column("#0",width=0, stretch=NO)
tabla.column("ID", width = 70)
tabla.column("Nombre", width = 200)
tabla.column("Cantidad", width = 80)
tabla.column("Costo Compra", width = 100)
tabla.column("Precio Venta", width = 100)
tabla.column("Fecha de vencimiento", width = 200)

tabla.heading("#0", text = "", anchor = CENTER)
tabla.heading("ID", text = "ID", anchor = CENTER)
tabla.heading("Nombre", text = "Nombre", anchor = CENTER)
tabla.heading("Cantidad", text = "Cantidad", anchor = CENTER)
tabla.heading("Costo Compra", text = "Costo Compra", anchor = CENTER)
tabla.heading("Precio Venta", text = "Precio Venta", anchor = CENTER)
tabla.heading("Fecha de vencimiento", text = "Fecha de vencimiento", anchor = CENTER)

tabla.place(x=100, y=600)

#-------------------------------------
def añadir_producto():
    df = pd.read_csv("./Database/productos.csv")
    nombre = nombre_producto.get()
    cantidad = cantidad_producto.get()
    messagebox.showinfo("Éxito","Producto guardado con éxito")


añadir_b = Button(
    Ingresar_p,
    text = "Añadir producto",
    command = añadir_producto,
    borderwidth=0,
    activebackground="#1E4024",
    activeforeground="#FFFFFF"
)

añadir_b.configure(
    font = ("Bahnschrift", 12),
    fg = "#FFFFFF",
    bg = "#1E4024"
)

añadir_b.place(x=50, y=350)







Ingresar_p.mainloop()