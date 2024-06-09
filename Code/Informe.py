from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import subprocess
import pandas as pd
import datetime
import matplotlib.pyplot as plt

informe_p = Tk()

informe_p.title("Informe")
informe_p.resizable(True, True)
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

screenwidth = informe_p.winfo_screenwidth()
screenheight = informe_p.winfo_screenheight()

x = (screenwidth / 2) - (1000 / 2)
y = (screenheight / 2) - (750 / 2)

informe_p.geometry("%dx%d+%d+%d" % (1000, 750, x, y))

tabla = ttk.Treeview(
    informe_p
)

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

#------------Bucle que añade los productos de baja rotacion y agotados en la tabla----------------------

for index, row in df.iterrows():
    if row['Cantidad'] >= 75:
        tabla.insert("", "end", values=(row['ID'], row['Nombre'], "Baja Rotación")) #Si cumple la condicion pone baja rotación
    elif row['Cantidad'] == 0:
        tabla.insert("", "end", values=(row['ID'], row['Nombre'], "Agotado")) #Si cumple la condicion pone agotado

tabla.place(x=50, y=100)

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

#-----------------Funcion para generar el informe-------------------

def generar_informe():
    fecha_inicio_str = fecha_inicio_entry.get() #Obtiene la fecha de inicio
    fecha_fin_str = fecha_fin_entry.get() #Obtiene la fecha de fin
    
    try:
        fecha_inicio = datetime.datetime.strptime(fecha_inicio_str, "%Y-%m-%d") #Convierte la fecha de inicio a un formato de fecha
        fecha_fin = datetime.datetime.strptime(fecha_fin_str, "%Y-%m-%d") #Convierte la fecha de fin a un formato de fecha
    except ValueError:
        messagebox.showerror("Error", "Formato de fecha incorrecto. Use YYYY-MM-DD.")
        return
    
    if fecha_fin < fecha_inicio:
        messagebox.showerror("Error", "Rango de fecha incorrecto, fecha fin es menor a la fecha de inicio.")
        return
    
    ventas = []

    try:
        with open('./Database/facturas.txt', 'r') as file:
            for linea in file: #Recorre las lineas del archivo
                partes = linea.strip().split(", ")  # Separa la linea en partes
                if len(partes) < 4: #Si la linea no tiene 4 partes, continua
                    continue

                id_factura = partes[0].split(": ")[1] #Obtiene el id de la factura
                id_cliente = partes[1].split(": ")[1] #Obtiene el id del cliente
                fecha_factura_str = partes[2].split(": ")[1] #Obtiene la fecha de la factura
                total_factura = float(partes[3].split(": ")[1][1:]) #Obtiene el total de la factura

                fecha_factura = datetime.datetime.strptime(fecha_factura_str, "%Y-%m-%d") #Convierte la fecha de la factura a un formato de fecha

                if fecha_inicio <= fecha_factura <= fecha_fin: #Si la fecha de la factura esta en el rango de fechas seleccionado
                    ventas.append({ #Añade la venta a la lista de ventas
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

    total_ventas = sum(venta["Total Factura"] for venta in ventas) #Suma el total de las ventas en el rango de fechas seleccionado

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

#---------------Gráfico de ventas por fecha------------------
    
    fechas = [venta['Fecha Factura'] for venta in ventas] #Obtiene las fechas de las ventas
    totales = [venta['Total Factura'] for venta in ventas] #Obtiene los totales de las ventas

    plt.figure(figsize=(10, 5)) #Tamaño de la figura del grafico
    plt.plot(fechas, totales, marker='o') #Grafica las ventas por fecha con un marcador 'o'
    plt.title('Ventas por Fecha') #Titulo del grafico
    plt.xlabel('Fecha') #Etiqueta del eje x
    plt.ylabel('Total Ventas') #Etiqueta del eje y
    plt.xticks(rotation=45) #Rota las fechas 45 grados
    plt.tight_layout() #Ajusta el tamaño del grafico
    plt.savefig('./Database/ventas_por_fecha.png') 
    plt.close() 

    messagebox.showinfo("Informe", f"¡Informe generado! \n\nTotal de ventas: ${total_ventas}\nInforme guardado en: 'informe_ventas.txt' y 'ventas_por_fecha.png'.")

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



