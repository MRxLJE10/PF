from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import subprocess
import pandas as pd
import datetime

informe_p = Tk()

informe_p.title("Informe")
informe_p.resizable(False, False)
informe_p.configure(bg="#1E4024")


def volver():
    informe_p.destroy()
    subprocess.call(["python", "Code/Menu_principal.py"])

volver_b = Button(
    informe_p,
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
screenwidth = informe_p.winfo_screenwidth()
screenheight = informe_p.winfo_screenheight()

x = (screenwidth / 2) - (1000 / 2)
y = (screenheight / 2) - (900 / 2)

informe_p.geometry("%dx%d+%d+%d" % (1000, 900, x, y))


tabla = ttk.Treeview(
    informe_p
)

# Carga el archivo csv con la libreria pandas (nombrada como pd)
df = pd.read_csv("./Database/productos.csv")

tabla['columns'] = ("ID", "Nombre Producto", "Estado")

tabla.column("#0", width=0, stretch=NO)
tabla.column("ID", width=70)
tabla.column("Nombre Producto", width=200)
tabla.column("Estado", width=100)

tabla.heading("#0", text="", anchor=CENTER)
tabla.heading("ID", text="ID", anchor=CENTER)
tabla.heading("Nombre Producto", text="Nombre", anchor=CENTER)
tabla.heading("Estado", text="Estado", anchor=CENTER)

for index, row in df.iterrows():
    if row['Cantidad'] >= 75:
        tabla.insert("", "end", values=(row['ID'], row['Nombre'], "Baja Rotación"))
    elif row['Cantidad'] == 0:
        tabla.insert("", "end", values=(row['ID'], row['Nombre'], "Agotado"))

tabla.place(x=50, y=100)

# Cuadro de texto para las fechas
fecha_inicio_label = Label(
    informe_p, 
    text="Fecha Inicio (YYYY-MM-DD):", 
    font=("Bahnschrift", 12), 
    fg="#FFFFFF", 
    bg="#1E4024"
)

fecha_inicio_label.place(x=50, y=500)

fecha_inicio_entry = Entry(
    informe_p
)

fecha_inicio_entry.place(x=255, y=500)

fecha_fin_label = Label(
    informe_p, 
    text="Fecha Fin (YYYY-MM-DD):", 
    font=("Bahnschrift", 12), 
    fg="#FFFFFF", 
    bg="#1E4024"
)

fecha_fin_label.place(x=50, y=550)

fecha_fin_entry = Entry(
    informe_p
)

fecha_fin_entry.place(x=250, y=550)

def generar_informe():
    fecha_inicio_str = fecha_inicio_entry.get()
    fecha_fin_str = fecha_fin_entry.get()
    
    try:
        fecha_inicio = datetime.datetime.strptime(fecha_inicio_str, "%Y-%m-%d")
        fecha_fin = datetime.datetime.strptime(fecha_fin_str, "%Y-%m-%d")
    except ValueError:
        messagebox.showerror("Error", "Formato de fecha incorrecto. Use YYYY-MM-DD.")
        return
    
    ventas = []

    try:
        with open('./Database/facturas.txt', 'r') as file:
            for linea in file:
                partes = linea.strip().split(", ")
                if len(partes) < 4:
                    continue

                id_factura = partes[0].split(": ")[1]
                id_cliente = partes[1].split(": ")[1]
                fecha_factura_str = partes[2].split(": ")[1]
                total_factura = float(partes[3].split(": ")[1][1:])

                fecha_factura = datetime.datetime.strptime(fecha_factura_str, "%Y-%m-%d")

                if fecha_inicio <= fecha_factura <= fecha_fin:
                    ventas.append({
                        "ID Factura": id_factura,
                        "ID Cliente": id_cliente,
                        "Fecha Factura": fecha_factura_str,
                        "Total Factura": total_factura,
                    })
    except FileNotFoundError:
        messagebox.showerror("Error", "El archivo facturas.txt no existe.")
        return

    if not ventas:
        messagebox.showinfo("Informe", "No hay ventas en el rango de fechas seleccionado.")
        return

    total_ventas = sum(venta["Total Factura"] for venta in ventas)

    # Guarda el informe en el txt
    with open('./Database/informe_ventas.txt', 'w') as f:
        f.write("========================================\n")
        f.write("********** Informe de Ventas ***********\n")
        f.write(f"******{fecha_inicio_str} hasta {fecha_fin_str}*******\n")
        f.write("========================================\n")
        for venta in ventas:
            f.write(f"ID Factura: {venta['ID Factura']}, ID Cliente: {venta['ID Cliente']}, Fecha: {venta['Fecha Factura']}, Total: ${venta['Total Factura']}\n")
        f.write("\n========================================")
        f.write(f"\nTotal de Ventas: ${total_ventas}\n")
        f.write("========================================\n")

    messagebox.showinfo("Informe", f"Informe generado. Total de ventas: ${total_ventas}\nInforme guardado en 'informe_ventas.txt'.")

generar_informe_button = Button(
    informe_p,
    text="Generar Informe",
    command=generar_informe,
    borderwidth=0,
    activebackground="#1E4024",
    activeforeground="#FFFFFF"
)
generar_informe_button.configure(
    font=("Bahnschrift", 12),
    fg="#FFFFFF",
    bg="#1E4024"
)
generar_informe_button.place(x=250, y=600)

informe_p.mainloop()


