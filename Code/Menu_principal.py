from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import subprocess
from PIL import Image, ImageTk

Menu_principal = Tk()
Menu_principal.title("Menu principal")
Menu_principal.geometry("800x600")
Menu_principal.resizable(False, False)
Menu_principal.configure(bg="#1E4024")

screenwidth = Menu_principal.winfo_screenwidth()
screenheight = Menu_principal.winfo_screenheight()

x = (screenwidth/2) - (800/2)
y = (screenheight/2) - (600/2)

Menu_principal.geometry("%dx%d+%d+%d" % (800, 600, x, y))
Menu_principal.resizable(False, False)


image = Image.open("Image/MENU_PRINCIPAL.png")
image = image.resize((800, 600))
photo = ImageTk.PhotoImage(image)
label = Label(image=photo)
label.place(x=0, y=0)

def ingresar_productos():
    Menu_principal.destroy()
    subprocess.call(["python", "Code/Ingresar_producto.py"])
    
def hacer_ventas():
    Menu_principal.destroy()
    subprocess.call(["python", "Code/Ventas.py"])

def informe_p():
    Menu_principal.destroy()
    subprocess.call(["python", "Code/Informe.py"])
    
def volver():
    Menu_principal.destroy()
    subprocess.call(["python", "Code/PF.py"])

def registrar_cliente():
    Menu_principal.destroy()
    subprocess.call(["python", "Code/Registrar_cliente.py"])

#Boton volver
volver_b = Button(
    Menu_principal,
    text = "Volver",
    command = volver,
    borderwidth=0,
    activebackground="#C4901E",
    activeforeground="#FFFFFF"
)

volver_b.configure(
    font = ("Bahnschrift", 12),
    fg = "#FFFFFF",
    bg = "#C4901E"
)

volver_b.place(x=70, y=10)

producto = Button(
    Menu_principal,
    text = "Ingresar Producto",
    command = ingresar_productos,
    borderwidth=0,
    activebackground="#1E4024",
    activeforeground="#FFFFFF"
)

producto.configure(
    font = ("Bahnschrift", 12),
    fg = "#FFFFFF",
    bg = "#1E4024"
)
producto.place(x=325, y=140)


ventas = Button(
    Menu_principal,
    text = "Ventas",
    command = hacer_ventas,
    borderwidth=0,
    activebackground="#1E4024",
    activeforeground="#FFFFFF"
)

ventas.configure(
    font = ("Bahnschrift", 12),
    fg = "#FFFFFF",
    bg = "#1E4024"
)
ventas.place(x=365, y=255)



informe = Button(
    Menu_principal,
    text = "Informe",
    command = informe_p,
    borderwidth=0,
    activebackground="#1E4024",
    activeforeground="#FFFFFF"
)

informe.configure(
    font = ("Bahnschrift", 12),
    fg = "#FFFFFF",
    bg = "#1E4024"
)
informe.place(x=365, y=367)

reg_cliente = Button(
    Menu_principal,
    borderwidth=0,
    text="Registrar Cliente",
    command=registrar_cliente,
    activebackground="#1E4024",
    activeforeground="#FFFFFF"
)

reg_cliente.configure(
    font=("Bahnschrift", 12),
    bg="#1E4024",
    fg="#FFFFFF",
)

reg_cliente.place(x=334, y=480)




Menu_principal.mainloop()