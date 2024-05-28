from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import subprocess
from PIL import Image, ImageTk

register = Tk()

register.title("Registrar")
register.geometry("500x500")
register.resizable(False, False)
register.configure(bg="#1E4024")

#Esto posiciona en la mitad la ventana
screenwidth = register.winfo_screenwidth()
screenheight = register.winfo_screenheight()

x = (screenwidth/2) - (500/2)
y = (screenheight/2) - (500/2)

register.geometry("%dx%d+%d+%d" % (500, 500, x, y))

image = Image.open("Image/Registrar.png")
image = image.resize((500, 500))
photo = ImageTk.PhotoImage(image)
label = Label(image=photo)
label.place(x=0, y=0)

#------------Boton para volver-------------
def back():
    register.destroy()
    subprocess.call(["python", "Code/PF.py"])

button_back = Button(
    register, 
    text="Volver", 
    command=back,
    borderwidth=0,
    activebackground="#1E4024",
    activeforeground="#FFFFFF"
)

button_back.configure(
    font = ("Bahnschrift", 12),
    bg="#1E4024",
    fg="#FFFFFF"
)

button_back.place(x=10, y=10)

#---------Funcion registrar usuario-----------

def registrar_usuario():
    usuarios_registrados = []
    primary_key = 1

    try:
        with open('./Database/Usuarios.txt', 'r') as archivo:
            usuarios_registrados = archivo.readlines()
            if usuarios_registrados:
                # Obtiene la llave primaria del ultimo usuario registrado
                primary_key = int(usuarios_registrados[-1].split(',')[0]) + 1
    except FileNotFoundError:
        pass

    # verifica si el usuario ya existe
    if any(f'{nombre_entry.get()},{fechaNacimiento_entry.get()},{documento_entry.get()}' in usuario for usuario in usuarios_registrados):
        messagebox.showerror("Tenemos un errorsillo muchachon", "El usuario ya existe")
        documento_entry.delete(0, END)
        return

    #abre el archivo para añadir el nuevo usuario
    with open('./Database/Usuarios.txt','a') as f:
        f.write(f'{primary_key},{nombre_entry.get()},{fechaNacimiento_entry.get()},{documento_entry.get()}\n')
        messagebox.showinfo("Exito muchachon", "Usuario registrado con exito")
            

button_registrar = Button(
    register, 
    text="Registrar",
    command=registrar_usuario,
    borderwidth=0,
    activebackground="#1E4024",
    activeforeground="#FFFFFF"
)

button_registrar.configure(
    font = ("Bahnschrift", 12),
    fg = "#FFFFFF",
    bg = "#1E4024"
)

button_registrar.place(x=204, y=435)

#-----------Labels y entrys------------

nombre_label = Label(
    register, 
    text="Nombre",
    borderwidth=0
)

nombre_label.configure(
    font = ("Bahnschrift", 12),
    fg="#FFFFFF",
    bg="#1E4024"
)

nombre_label.place(x = 210, y = 160)

nombre_entry = Entry(
    register
)

nombre_entry.place(x = 180, y = 200)



fechaNacimiento_label = Label(
    register, 
    text="Fecha de Nacimiento",
    borderwidth=0
)

fechaNacimiento_label.configure(
    fg="#FFFFFF",
    font = ("Bahnschrift", 12),
    bg="#1E4024"
)

fechaNacimiento_label.place(x = 167, y = 240)

fechaNacimiento_entry = Entry(
    register
)

fechaNacimiento_entry.place(x = 180, y = 280)

documento_label = Label(
    register, 
    text="Numero documento",
    borderwidth=0
)

documento_label.configure(
    font = ("Bahnschrift", 12),
    fg="#FFFFFF",
    bg="#1E4024"
)

documento_label.place(x = 167, y = 320)

documento_entry = Entry(
    register
)

documento_entry.place(x = 180, y = 360)




register.mainloop()