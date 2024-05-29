from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import subprocess
import pandas as pd 


ventas = Tk()

ventas.title("Ventas")
ventas.resizable(False,False)
ventas.configure(bg="#1E4024")


def volver():
    ventas.destroy()
    subprocess.call(["python","Code/Menu_principal.py"])

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

carrito_button = Button(
    ventas,
    text = "Agregar al carrito",
    borderwidth=0,
    activebackground="#1E4024",
    activeforeground="#FFFFFF"
)

carrito_button.configure(
    font = ("Bahnschrift", 12),
    fg = "#FFFFFF",
    bg = "#1E4024"
)

carrito_button.place(x = 90, y = 200)



venta_button = Button(
    ventas,
    text = "Realizar venta",
    borderwidth=0,
    activebackground="#1E4024",
    activeforeground="#FFFFFF"
)

venta_button.configure(
    font = ("Bahnschrift", 12),
    fg = "#FFFFFF",
    bg = "#1E4024"
)

venta_button.place(x = 300, y = 200)




ventas.mainloop()