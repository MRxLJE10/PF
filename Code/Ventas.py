from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import subprocess

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






ventas.mainloop()