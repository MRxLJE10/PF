from tkinter import *
from tkinter import ttk
import subprocess
import pandas as pd
from tkinter import messagebox
import datetime
import numpy as np

Ingresar_p = Tk()

Ingresar_p.title("Ingresar Producto")
Ingresar_p.resizable(False,False)
Ingresar_p.configure(bg="#1E4024")

#Mide las dimensiones de la pantalla y posiciona la pantalla en el centro
screenwidth = Ingresar_p.winfo_screenwidth()
screenheight = Ingresar_p.winfo_screenheight()

x = (screenwidth/2) - (900/2)
y = (screenheight/2) - (730/2)

Ingresar_p.geometry("%dx%d+%d+%d" % (900, 730, x, y))

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

nombre.place(x = 50,y = 70)


nombre_producto = Entry(
    Ingresar_p
)

nombre_producto.place(x = 65, y = 110)


#------------------------------------

#Recuadro para ingresar la cantidad de producto
cantidad = Label(
    Ingresar_p,
    text = "Cantidad del producto",
    font = ("Bahnschrift", 12),
    fg = "#FFFFFF",
    bg = "#1E4024"
)

cantidad.place(x = 230,y = 70)


cantidad_producto = Entry(
    Ingresar_p
)

cantidad_producto.place(x = 250, y = 110)

#-------------------------------------

#Recuadro para ingresar el costo de producto
costoCompra = Label(
    Ingresar_p,
    text = "Costo de compra",
    font = ("Bahnschrift", 12),
    fg = "#FFFFFF",
    bg = "#1E4024"
)

costoCompra.place(x = 430,y = 70)


costo_compra = Entry(
    Ingresar_p
)

costo_compra.place(x = 430, y = 110)

#-------------------------------------

#Recuadro para ingresar el precio de venta
precio_venta = Label(
    Ingresar_p,
    text = "Precio de venta",
    font = ("Bahnschrift", 12),
    fg = "#FFFFFF",
    bg = "#1E4024"
)

precio_venta.place(x = 65,y = 150)


precio_v = Entry(
    Ingresar_p
)

precio_v.place(x = 65, y = 190)

#-------------------------------------

#Recuadro para ingresar la fecha de vencimiento
fecha_vence = Label(
    Ingresar_p,
    text = "Fecha Vencimiento",
    font = ("Bahnschrift", 12),
    fg = "#FFFFFF",
    bg = "#1E4024"
)

fecha_vence.place(x = 245,y = 150)


fecha_v = Entry(
    Ingresar_p
)

fecha_v.place(x = 250, y = 190)

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

tabla.place(x=65, y=400)


#Carga los datos de la tabla
def actualizar_tabla():
    # Borra todos los elementos de la tabla
    for i in tabla.get_children():
        tabla.delete(i)

    # Vuelve a llenar la tabla con los datos actualizados
    try:
        df = pd.read_csv('./Database/productos.csv', encoding='utf-8')
    except pd.errors.EmptyDataError:
        return

    for index, row in df.iterrows():
        tabla.insert("", "end", values=list(row))


def añadir_producto():
    # Toma lo que hay en los entrys y los almacena en variables
    nombre = nombre_producto.get()
    cantidad = cantidad_producto.get()
    costoCompra = costo_compra.get()
    precio = precio_v.get()
    fecha = fecha_v.get()

    if int(cantidad) < 0:
        # Muestra un mensaje de error si la cantidad es negativa
        messagebox.showerror("Error muchachon", "La cantidad no puede ser negativa no leiste el proyecto o que?")
        return

    # Valida que los campos no esten vacios
    try:
        df = pd.read_csv("./Database/productos.csv")
    except pd.errors.EmptyDataError:
        df = pd.DataFrame(columns=['ID', 'nombre', 'cantidad', 'costoCompra', 'precio', 'fecha'])

    while True:
        id = np.random.randint(100, 999)
        if id not in df['ID'].values:
            break

    producto = pd.DataFrame([[id, nombre, cantidad, costoCompra, precio, fecha]],
                            columns=df.columns)

    df = pd.concat([df, producto], ignore_index=True)
    df.to_csv("./Database/productos.csv", index=False, na_rep='')

    # Llama a actualizar_tabla después de añadir el producto
    actualizar_tabla()

def on_focus(event):
    actualizar_tabla()

# Asume que 'ventana' es el objeto de la ventana de Tkinter
Ingresar_p.bind('<FocusIn>', on_focus)
#-------------------------------------

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

añadir_b.place(x=250, y=290)







Ingresar_p.mainloop()