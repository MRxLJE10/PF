from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import subprocess
import pandas as pd 
import json
import os
from datetime import datetime

ventas = Tk()

ventas.title("Ventas")
ventas.resizable(False,False)
ventas.configure(bg="#1E4024")

# Variable global para el contador de facturas
contador_facturas = 0

# Ruta del archivo para guardar el número de la última factura
archivo_contador_facturas = './Database/contador_facturas.txt'

# Verificar si el archivo existe
if os.path.exists(archivo_contador_facturas):
    # Si existe, cargar el número de la última factura
    with open(archivo_contador_facturas, 'r') as archivo:
        contador_facturas = int(archivo.read())
else:
    # Si no existe, establecer el contador en 1
    contador_facturas = 1


def volver():
    ventas.destroy()
    subprocess.call(["python","Code/Menu_principal.py"])
    # Reiniciar el contador de facturas
    contador_facturas = 1


volver_b = Button(
    ventas,
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

#Mide las dimensiones de la pantalla y posiciona la pantalla en el centro
screenwidth = ventas.winfo_screenwidth()
screenheight = ventas.winfo_screenheight()

x = (screenwidth/2) - (1000/2)
y = (screenheight/2) - (900/2)

ventas.geometry("%dx%d+%d+%d" % (1000, 900, x, y))

#----------------------------------------------

tabla = ttk.Treeview(
    ventas
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
        
def on_focus(event):
    actualizar_tabla()

# Asume que 'ventana' es el objeto de la ventana de Tkinter
ventas.bind('<FocusIn>', on_focus)


id_label = Label(
    ventas,
    text = "ID Producto",
    borderwidth=0
)

id_label.configure(
    font = ("Bahnschrift", 12),
    fg="#FFFFFF",
    bg="#1E4024"
)

id_label.place(x = 100, y = 100)

id_entry = Entry(
    ventas
)

id_entry.place(x = 100, y = 130)

cantidad_label = Label(
    ventas,
    text = "Cantidad",
    borderwidth=0
)

cantidad_label.configure(
    font = ("Bahnschrift", 12),
    fg="#FFFFFF",
    bg="#1E4024"
)

cantidad_label.place(x = 300, y = 100)

cantidad_entry = Entry(
    ventas
)

cantidad_entry.place(x = 300, y = 130)


#----------------------Función que hace la venta----------------------

try:
    with open('./Database/contador_facturas.json', 'r') as f:
        contador_facturas = json.load(f)
except FileNotFoundError:
    # Si el archivo no existe, inicializa contador_facturas a 0
    contador_facturas = 0

def realizar_venta():
    global contador_facturas

    id_producto = id_entry.get()
    try:
        cantidad_vendida = int(cantidad_entry.get())
    except ValueError:
        messagebox.showerror("Error", "Cantidad debe ser un número")
        return

    with open('./Database/Usuario_actual.json', 'r') as archivo:
        datos_cargados = json.load(archivo)
        usuario_actual = datos_cargados['usuario_actual']

    # Verifica si hay productos en el carrito
    contenido_carrito = visualizador.get('1.0', 'end-1c').strip()
    if contenido_carrito == "Carrito de compras:" or contenido_carrito == "":
        messagebox.showerror("Error", "El carrito está vacío")
        return

    # Lee los datos de los productos desde el archivo CSV
    df = pd.read_csv("./Database/productos.csv")

    # Verifica si el producto existe en la base de datos
    try:
        id_producto = int(id_producto)
    except ValueError:
        messagebox.showerror("Error", "ID de producto debe ser un número")
        return

    if id_producto not in df['ID'].values:
        messagebox.showerror("Error", "ID de producto no encontrado")
        return

    # Encuentra el índice del producto que se está vendiendo
    indice_producto = df.loc[df['ID'] == id_producto].index[0]

    # Verifica si hay suficiente cantidad del producto
    cantidad_actual = df.at[indice_producto, 'Cantidad']
    if cantidad_vendida > cantidad_actual:
        messagebox.showerror("Error", "Cantidad insuficiente en inventario")
        return

    # Actualiza la cantidad del producto
    df.at[indice_producto, 'Cantidad'] = cantidad_actual - cantidad_vendida

    # Escribe los datos de los productos actualizados de nuevo en el archivo CSV
    df.to_csv("./Database/productos.csv", index=False)

    # Incrementa el contador de facturas después de realizar todas las verificaciones
    contador_facturas += 1

    # Guarda el contador de facturas en un archivo
    with open('./Database/contador_facturas.json', 'w') as f:
        json.dump(contador_facturas, f)

    # Definir la ruta de la carpeta donde se guardarán las facturas
    ruta_carpeta_facturas = './Database/'

    # Verificar si la carpeta de facturas existe, si no, crearla
    if not os.path.exists(ruta_carpeta_facturas):
        os.makedirs(ruta_carpeta_facturas)

    # Guardar la factura en un archivo de texto con el número de factura actual
    nombre_archivo_factura = f'{ruta_carpeta_facturas}factura_{contador_facturas}.txt'
    with open(nombre_archivo_factura, 'w') as f:
        f.write(contenido_carrito)

    messagebox.showinfo("Venta realizada", "La venta ha sido realizada exitosamente")

    actualizar_tabla()

    # Limpia las entradas y el visualizador
    id_entry.delete(0, END)
    cantidad_entry.delete(0, END)
    visualizador.configure(state='normal')
    visualizador.delete('1.0', END)
    visualizador.insert('end', "Carrito de compras:\n")
    visualizador.configure(state='disabled')

venta_button = Button(
    ventas,
    text = "Realizar venta",
    borderwidth=0,
    activebackground="#1E4024",
    activeforeground="#FFFFFF",
    command=realizar_venta
)

venta_button.configure(
    font = ("Bahnschrift", 12),
    fg = "#FFFFFF",
    bg = "#1E4024"
)

venta_button.place(x = 300, y = 200)

#----------------------Función que agrega productos al carrito----------------------

# Función para buscar un producto por su ID
def buscar_producto(id_producto):
    try:
        df = pd.read_csv('./Database/productos.csv', encoding='utf-8')
    except pd.errors.EmptyDataError:
        return
# Busca el producto con el ID dado
    for index, row in df.iterrows():
        if str(row['ID']) == id_producto:
            return row

    return None

# Función para agregar productos al carrito
def agregar_texto():
    id_producto = id_entry.get()
    producto = buscar_producto(id_producto)
    try:
        cantidad = int(cantidad_entry.get())
    except ValueError:
        messagebox.showerror("Error", "Cantidad debe ser un número")
        return

    if producto is None:
        messagebox.showerror("Error", "Producto no encontrado")
        return

    nombre_producto = producto['Nombre']
    cantidad_disponible = producto['Cantidad']

    if cantidad > cantidad_disponible:
        messagebox.showerror("Error", "Cantidad insuficiente en inventario")
        return

    visualizador.configure(state='normal')
    visualizador.insert('end', f"{cantidad} {nombre_producto}\n")
    visualizador.configure(state='disabled')

visualizador = Text(
    ventas,
    width=50,
    height=20,
    state=NORMAL
)
visualizador.insert('end', "Carrito de compras:\n")

visualizador.configure(state=DISABLED)

visualizador.place(x=500, y=100)

carrito_button = Button(
    ventas,
    text = "Agregar al carrito",
    borderwidth=0,
    activebackground="#1E4024",
    activeforeground="#FFFFFF",
    command=agregar_texto
)

carrito_button.configure(
    font = ("Bahnschrift", 12),
    fg = "#FFFFFF",
    bg = "#1E4024"
)

carrito_button.place(x = 90, y = 200)

ventas.mainloop()