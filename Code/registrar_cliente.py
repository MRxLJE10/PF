from tkinter  import *
from tkinter import ttk
import subprocess
from PIL import Image, ImageTk
from tkinter import messagebox


reg_cliente = Tk()

reg_cliente.title("Registrar")
reg_cliente.geometry("500x500")
reg_cliente.resizable(False, False)
reg_cliente.configure(bg="#1E4024")

#Esto posiciona en la mitad la ventana
screenwidth = reg_cliente.winfo_screenwidth()
screenheight = reg_cliente.winfo_screenheight()

x = (screenwidth/2) - (500/2)
y = (screenheight/2) - (500/2)

reg_cliente.geometry("%dx%d+%d+%d" % (500, 500, x, y))

image = Image.open("Image/Registrar_cliente.png")
image = image.resize((500, 500))
photo = ImageTk.PhotoImage(image)
label = Label(image=photo)
label.place(x=0, y=0)


#------------Boton para volver-------------
def volver():
    reg_cliente.destroy()
    subprocess.call(["python","Code/Menu_principal.py"])

volver_b = Button(
    reg_cliente,
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

#---------Funcion registrar usuario-----------

def registrar_cliente():
    cliente_registrado = []
    primary_key = 1

    try:
        with open('./Database/Clientes.txt', 'r') as archivo:
            cliente_registrado = archivo.readlines()
            if cliente_registrado:
                # Obtiene la llave primaria del ultimo cliente registrado
                primary_key = int(cliente_registrado[-1].split(',')[0]) + 1
    except FileNotFoundError:
        pass

    # verifica si el documento ya existe
    if any(documento_entry.get() in usuario.split(',')[3] for usuario in cliente_registrado):
        messagebox.showerror("Tenemos un errorsillo muchachon", "El documento ya está registrado")
        documento_entry.delete(0, END)
        return

    # abre el archivo para añadir el nuevo cliente
    with open('./Database/Clientes.txt','a') as f:
        f.write(f'{primary_key},{nombre_entry.get()},{fechaNacimiento_entry.get()},{documento_entry.get()}\n')
        messagebox.showinfo("Exito muchachon", "Cliente registrado con exito")
            

button_registrar = Button(
    reg_cliente, 
    text="Registrar",
    command=registrar_cliente,
    borderwidth=0,
    activebackground="#1E4024",
    activeforeground="#FFFFFF"
)

button_registrar.configure(
    font = ("Bahnschrift", 12),
    fg = "#FFFFFF",
    bg = "#1E4024"
)

button_registrar.place(x=204, y=448)

#-----------Labels y entrys------------

nombre_label = Label(
    reg_cliente, 
    text="Nombre",
    borderwidth=0
)

nombre_label.configure(
    font = ("Bahnschrift", 12),
    fg="#FFFFFF",
    bg="#1E4024"
)

nombre_label.place(x = 210, y = 185)

nombre_entry = Entry(
    reg_cliente
)

nombre_entry.place(x = 180, y = 225)



fechaNacimiento_label = Label(
    reg_cliente, 
    text="Fecha de Nacimiento",
    borderwidth=0
)

fechaNacimiento_label.configure(
    fg="#FFFFFF",
    font = ("Bahnschrift", 12),
    bg="#1E4024"
)

fechaNacimiento_label.place(x = 167, y = 265)

fechaNacimiento_entry = Entry(
    reg_cliente
)

fechaNacimiento_entry.place(x = 180, y = 305)

documento_label = Label(
    reg_cliente, 
    text="Numero documento",
    borderwidth=0
)

documento_label.configure(
    font = ("Bahnschrift", 12),
    fg="#FFFFFF",
    bg="#1E4024"
)

documento_label.place(x = 167, y = 345)

documento_entry = Entry(
    reg_cliente
)

documento_entry.place(x = 180, y = 385)


reg_cliente.mainloop()