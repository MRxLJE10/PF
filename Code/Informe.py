from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import subprocess

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






informe_p.mainloop()