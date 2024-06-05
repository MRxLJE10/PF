from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import subprocess
import pandas as pd

informe_p = Tk()

informe_p.title("Informe")
informe_p.resizable(False,False)
informe_p.configure(bg="#1E4024")


def volver():
    informe_p.destroy()
    subprocess.call(["python","Code/Menu_principal.py"])

volver_b = Button(
    informe_p,
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
screenwidth = informe_p.winfo_screenwidth()
screenheight = informe_p.winfo_screenheight()

x = (screenwidth/2) - (1000/2)
y = (screenheight/2) - (900/2)

informe_p.geometry("%dx%d+%d+%d" % (1000, 900, x, y))


tabla = ttk.Treeview(
    informe_p
)

#Carga el archivo csv con la libreria pandas(nombrada como pd)
df = pd.read_csv("./Database/productos.csv")

tabla['columns'] = ("ID","Nombre Producto", "Cantidad", "Estado")

tabla.column("#0",width=0, stretch=NO)
tabla.column("ID", width = 70)
tabla.column("Nombre Producto", width = 200)
tabla.column("Cantidad", width = 80)
tabla.column("Estado", width = 100)

tabla.heading("#0", text = "", anchor = CENTER)
tabla.heading("ID", text = "ID", anchor = CENTER)
tabla.heading("Nombre Producto", text = "Nombre", anchor = CENTER)
tabla.heading("Cantidad", text = "Cantidad", anchor = CENTER)
tabla.heading("Estado", text = "Estado", anchor = CENTER)

for index, row in df.iterrows():
    if row['Cantidad'] >= 75:
        tabla.insert("", "end", values=(row['ID'], row['Nombre'], row['Cantidad'], "Baja Rotación"))
    elif row['Cantidad'] == 0:
        tabla.insert("", "end", values=(row['ID'], row['Nombre'], row['Cantidad'], "Agotado"))


tabla.place(x=50, y=100)











informe_p.mainloop()