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
ventas.resizable(False, False)
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
    subprocess.call(["python", "Code/Menu_principal.py"])
    # Reiniciar el contador de facturas
    contador_facturas = 1

volver_b = Button(
    ventas,
    text="Volver",
    command=volver,
    borderwidth=0,
    activebackground="#1E4024",
    activeforeground="#FFFFFF"
)
volver_b.configure(
    font=("Bahnschrift", 12),
    fg="#FFFFFF",
    bg="#1E4024"
)

volver_b.place(x=10, y=10)

# Mide las dimensiones de la pantalla y posiciona la pantalla en el centro
screenwidth = ventas.winfo_screenwidth()
screenheight = ventas.winfo_screenheight()

x = (screenwidth / 2) - (1000 / 2)
y = (screenheight / 2) - (900 / 2)

ventas.geometry("%dx%d+%d+%d" % (1000, 900, x, y))

#----------------------------------------------

tabla = ttk.Treeview(
    ventas
)

# Carga el archivo csv con la libreria pandas(nombrada como pd)
df = pd.read_csv("./Database/productos.csv")

tabla['columns'] = ("ID", "Nombre", "Cantidad", "Costo Compra", "Precio Venta", "Fecha de vencimiento")

tabla.column("#0", width=0, stretch=NO)
tabla.column("ID", width=70)
tabla.column("Nombre", width=200)
tabla.column("Cantidad", width=80)
tabla.column("Costo Compra", width=100)
tabla.column("Precio Venta", width=100)
tabla.column("Fecha de vencimiento", width=200)

tabla.heading("#0", text="", anchor=CENTER)
tabla.heading("ID", text="ID", anchor=CENTER)
tabla.heading("Nombre", text="Nombre", anchor=CENTER)
tabla.heading("Cantidad", text="Cantidad", anchor=CENTER)
tabla.heading("Costo Compra", text="Costo Compra", anchor=CENTER)
tabla.heading("Precio Venta", text="Precio Venta", anchor=CENTER)
tabla.heading("Fecha de vencimiento", text="Fecha de vencimiento", anchor=CENTER)

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
    text="ID Producto",
    borderwidth=0
)

id_label.configure(
    font=("Bahnschrift", 12),
    fg="#FFFFFF",
    bg="#1E4024"
)

id_label.place(x=100, y=100)

id_entry = Entry(
    ventas
)

id_entry.place(x=100, y=130)

cantidad_label = Label(
    ventas,
    text="Cantidad",
    borderwidth=0
)

cantidad_label.configure(
    font=("Bahnschrift", 12),
    fg="#FFFFFF",
    bg="#1E4024"
)

cantidad_label.place(x=300, y=100)

cantidad_entry = Entry(
    ventas
)

cantidad_entry.place(x=300, y=130)

#--------Funcion que Autocompleta apartir del Documento del cliente----------
def autocompletar(*args):
    documento_ingresado = doc_entry.get()
    with open("./Database/Clientes.txt", "r") as archivo:
        lineas = archivo.readlines()
        for linea in lineas:
            cliente_registrado = linea.split(",")
            documento = cliente_registrado[3].strip() 
            if documento == documento_ingresado:
                nom_entry.delete(0, END)
                nom_entry.insert(0, cliente_registrado[1])
                break
        else:
            nom_entry.delete(0, END)
    
        
doc_label = Label(
    ventas,
    text="N° Documento:",
    borderwidth=0
)

doc_label.configure(
    font=("Bahnschrift", 12),
    fg="#FFFFFF",
    bg="#1E4024"
)

doc_label.place(x=100, y=160)

doc_entry = Entry(
    ventas
)

doc_entry.place(x=100, y=190)

doc_entry.bind("<KeyRelease>", autocompletar)

nom_label = Label(
    ventas,
    text="Cliente:",
    borderwidth=0
)

nom_label.configure(
    font=("Bahnschrift", 12),
    fg="#FFFFFF",
    bg="#1E4024"
)

nom_label.place(x=300, y=160)

nom_entry = Entry(
    ventas
)

nom_entry.place(x=300, y=190)





monto_a_pagar_label = Label(
    ventas,
    text="Monto a pagar",
    borderwidth=0
)

monto_a_pagar_label.configure(
    font=("Bahnschrift", 12),
    fg="#FFFFFF",
    bg="#1E4024"
)

monto_a_pagar_label.place(x=100, y=230)

monto_a_pagar_entry = Entry(
    ventas
)

monto_a_pagar_entry.place(x=100, y=260)



#----------------------Función que hace la venta----------------------

try:
    with open('./Database/contador_facturas.json', 'r') as f:
        contador_facturas = json.load(f)
except FileNotFoundError:
    # Si el archivo no existe, inicializa contador_facturas a 0
    contador_facturas = 0

carrito = []


def realizar_venta():
    global contador_facturas
    global total_venta

    # Verifica si hay productos en el carrito
    if not carrito:
        messagebox.showerror("Error", "El carrito está vacío")
        return
    # Verifica si se ingresó el nombre del cliente
    nombre_cliente = nom_entry.get().strip()
    if not nombre_cliente:
        messagebox.showerror("Error", "Debe ingresar un documento válido de cliente")
        return

    # Verifica si el monto a pagar es un entero positivo
    try:
        monto_a_pagar = int(monto_a_pagar_entry.get())
        if monto_a_pagar <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Error", "El monto a pagar debe ser un entero positivo")
        monto_a_pagar_entry.delete(0, END)
        return

    # Calcula el total de la venta
    total_venta = 0
    df = pd.read_csv("./Database/productos.csv")
    for item in carrito:
        id_producto = item['ID']
        cantidad_vendida = item['Cantidad']
        indice_producto = df.loc[df['ID'] == int(id_producto)].index[0]
        precio_producto = df.at[indice_producto, 'Precio venta']
        total_venta += cantidad_vendida * precio_producto

    if monto_a_pagar < total_venta:
        messagebox.showerror("Error", "El monto a pagar es menor que el total de la venta")
        return

    # Descuenta los productos vendidos del inventario
    for item in carrito:
        id_producto = item['ID']
        cantidad_vendida = item['Cantidad']
        indice_producto = df.loc[df['ID'] == int(id_producto)].index[0]
        cantidad_actual = df.at[indice_producto, 'Cantidad']
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

    # Obtén la fecha y hora actual
    fecha_hora_actual = datetime.now().strftime('%Y-%m-%d')

    # Obtén el usuario actual
    with open('./Database/Usuario_actual.json', 'r') as f:
        Usuario_actual = json.load(f)

    # Guarda la factura en un archivo de texto
    nombre_archivo_factura = f'{ruta_carpeta_facturas}factura_{contador_facturas}.txt'
    with open(nombre_archivo_factura, 'w') as f:
        f.write("Rapitienda 'El Muchachon'\n")
        f.write(f"Factura numero: {contador_facturas}\n")
        f.write(f"Fecha y hora: {fecha_hora_actual}\n\n")
        f.write("---------------------------------------- \n\n")
        f.write(f"Venta realizada por: {Usuario_actual['usuario_actual']}\n")
        f.write(f"Nombre Cliente: {nom_entry.get()}\n")
        f.write(f"Documento Cliente: {doc_entry.get()}\n\n")
        f.write("---------------------------------------- \n\n")
        f.write("Productos comprados:\n")
        for item in carrito:
            id_producto = item['ID']
            nombre_producto = item['Nombre']
            cantidad_producto = item['Cantidad']
            precio_producto = df.loc[df['ID'] == int(id_producto), 'Precio venta'].values[0]
            total_producto = cantidad_producto * precio_producto
            f.write(f"{cantidad_producto} {nombre_producto} - C/U${precio_producto} Total producto: ${total_producto}\n")

        f.write("\n""---------------------------------------- \n\n")
        f.write(f"TOTAL: ${total_venta}\n")
        f.write(f"Efectivo: ${monto_a_pagar_entry.get()}\n")
        f.write(f"Cambio: ${monto_a_pagar - total_venta}\n")

    messagebox.showinfo("Venta realizada", "La venta ha sido realizada exitosamente")

    # Limpia las entradas y el visualizador
    id_entry.delete(0, END)
    cantidad_entry.delete(0, END)
    visualizador.configure(state='normal')
    visualizador.delete('1.0', END)
    visualizador.insert('end', "Carrito de compras:\n")
    visualizador.configure(state='disabled')
    doc_entry.delete(0, END)
    nom_entry.delete(0, END)
    monto_a_pagar_entry.delete(0, END)
    carrito.clear()
    actualizar_tabla()


venta_button = Button(
    ventas,
    text="Realizar venta",
    borderwidth=0,
    activebackground="#1E4024",
    activeforeground="#FFFFFF",
    command=realizar_venta
)

venta_button.configure(
    font=("Bahnschrift", 12),
    fg="#FFFFFF",
    bg="#1E4024"
)

venta_button.place(x=300, y=300)

#----------------------Función que agrega productos al carrito----------------------

def buscar_producto(id_producto):
    try:
        df = pd.read_csv('./Database/productos.csv', encoding='utf-8')
    except pd.errors.EmptyDataError:
        return None

    for index, row in df.iterrows():
        if str(row['ID']) == id_producto:
            return row

    return None

def agregar_a_carrito():
    id_producto = id_entry.get()
    cantidad = cantidad_entry.get()

    if not id_producto or not cantidad:
        messagebox.showerror("Error", "Debe ingresar un ID de producto y una cantidad")
        return

    try:
        cantidad = int(cantidad)
        if cantidad <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Error", "La cantidad debe ser un número entero positivo")
        return

    # Lee los datos de los productos desde el archivo CSV
    df = pd.read_csv("./Database/productos.csv")

    # Busca el producto en el inventario
    if int(id_producto) not in df['ID'].values:
        messagebox.showerror("Error", f"ID de producto {id_producto} no encontrado")
        return

    # Encuentra el indice
    indice_producto = df.loc[df['ID'] == int(id_producto)].index[0]

    nombre_producto = df.at[indice_producto, 'Nombre']

    carrito.append({
        'ID': id_producto,
        'Nombre': nombre_producto,
        'Cantidad': cantidad
    })

    # Actualiza el visualizador del carrito
    actualizar_visualizador_carrito()

def eliminar_ultimo_producto():
    if not carrito:
        messagebox.showerror("Error", "No hay productos en el carrito para eliminar")
        return

    carrito.pop()

    # Actualiza el visualizador del carrito
    actualizar_visualizador_carrito()

def actualizar_visualizador_carrito():
    contenido_carrito = "Carrito de compras:\n" + "\n".join([f"{item['Cantidad']} {item['Nombre']}" for item in carrito])

    visualizador.configure(state='normal')
    visualizador.delete('1.0', END)
    visualizador.insert('1.0', contenido_carrito)
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
    text="Agregar al carrito",
    borderwidth=0,
    activebackground="#1E4024",
    activeforeground="#FFFFFF",
    command=agregar_a_carrito
)

carrito_button.configure(
    font=("Bahnschrift", 12),
    fg="#FFFFFF",
    bg="#1E4024"
)

carrito_button.place(x=90, y=300)

eliminar_button = Button(
    ventas,
    text="Eliminar último producto",
    borderwidth=0,
    activebackground="#1E4024",
    activeforeground="#FFFFFF",
    command=eliminar_ultimo_producto
)

eliminar_button.configure(
    font=("Bahnschrift", 12),
    fg="#FFFFFF",
    bg="#1E4024"
)

eliminar_button.place(x=90, y=350)



ventas.mainloop()