#Proyecto final
#Integrantes:

#Librerias
from tkinter import *
from tkinter import ttk
import subprocess
from PIL import Image,ImageTk

inventario = Tk()

inventario.title("Inventario")
inventario.geometry("800x600")
screenwidth = inventario.winfo_screenwidth()
screenheight = inventario.winfo_screenheight()

x = (screenwidth/2) - (800/2)
y = (screenheight/2) - (600/2)

inventario.geometry("%dx%d+%d+%d" % (800, 600, x, y))
inventario.resizable(False, False)

image = Image.open("Image/Tienda.png")
image = image.resize((800, 600))
photo = ImageTk.PhotoImage(image)
label = Label(image=photo)
label.place(x=0, y=0)

#----------------------------------------------------------

def ingresar_usuario():
    inventario.destroy()
    subprocess.call(["python", "Code/Ingresar_usuario.py"])

ingresar_u = Button(
    inventario,
    borderwidth=0,
    text="Ingresar Usuario",
    command=ingresar_usuario,
    activebackground="#1E4024",
    activeforeground="#FFFFFF"
)

ingresar_u.configure(
    font=("Bahnschrift", 14),
    bg="#1E4024",
    fg="#FFFFFF",
)

ingresar_u.place(x=10, y=10)

#----------------------------------------------------------
def registrar_u():
    inventario.destroy()
    subprocess.call(["python", "Code/registrar.py"])

registrar_u = Button(
    inventario,
    borderwidth=0,
    text="Registrar Usuario",
    command=registrar_u,
    activebackground="#1E4024",
    activeforeground="#FFFFFF"
)

registrar_u.configure(
    font=("Bahnschrift", 14),
    bg="#1E4024",
    fg="#FFFFFF",
)

registrar_u.place(x=10, y=60)

inventario.mainloop()
