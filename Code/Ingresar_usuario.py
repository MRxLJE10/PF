from tkinter import *
from tkinter import ttk
import subprocess
from tkinter import messagebox
from PIL import Image, ImageTk
import json

Ingresar_usuario = Tk()

Ingresar_usuario.title("Ingresar Usuario")
Ingresar_usuario.geometry("500x500")
Ingresar_usuario.resizable(False,False)
Ingresar_usuario.configure(bg="#1E4024")

screenwidth = Ingresar_usuario.winfo_screenwidth()
screenheight = Ingresar_usuario.winfo_screenheight()

x = (screenwidth/2) - (500/2)
y = (screenheight/2) - (500/2)

Ingresar_usuario.geometry("%dx%d+%d+%d" % (500, 500, x, y))


image = Image.open("Image/Ingresar.png")
image = image.resize((500, 500))
photo = ImageTk.PhotoImage(image)
label = Label(image=photo)
label.place(x=0, y=0)

#-------------------Boton de volver-------------------

def volver():
    Ingresar_usuario.destroy()
    subprocess.call(["python","Code/PF.py" ])

#-------------------Funcion login-------------------

#funcion que ingresa al menu principal
def i_menu():
    Ingresar_usuario.destroy()
    subprocess.call(["python","Code/Menu_principal.py" ])



def verificar_iniciar():
    with open("./Database/Usuarios.txt", "r") as archivo:
        lineas = archivo.readlines()
        for linea in lineas:
            datos_usuario = linea.split(",")
            documento = datos_usuario[3].strip() 
            nombre_usuario = datos_usuario[1].strip()
            
            if documento == documento_entry.get():
                messagebox.showinfo("Bienvenido","Bienvenido muchachon")
                with open('./Database/Usuario_actual.json', 'w') as file:
                    json.dump({'usuario_actual': nombre_usuario}, file)
                documento_entry.delete(0, END)
                i_menu()
                return  #sale de la funcion al ingresar correctamente

        messagebox.showinfo("Error", "Usuario no encontrado")
        documento_entry.delete(0, END)

iniciar_b = Button(
    Ingresar_usuario,
    text = "Iniciar",
    command = verificar_iniciar,
    borderwidth=0,
    fg="#FFFFFF",
    bg="#1E4024",
    activebackground="#1E4024",
    activeforeground="#FFFFFF"
)

iniciar_b.configure(
    font = ("Bahnschrift", 12),
    fg = "#FFFFFF",
    bg = "#1E4024"
)

iniciar_b.place(x=212, y=435)

#----------------------------------------------------
    
volver_b = Button (
    Ingresar_usuario,
    text = "Volver",
    command= volver,
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



documento_label = Label(
    Ingresar_usuario,
    text = "Documento",
    borderwidth=0
)

documento_label.configure(
    font = ("Bahnschrift", 12),
    fg="#FFFFFF",
    bg="#1E4024"
)

documento_label.place(x = 197, y = 160)

documento_entry = Entry(
    Ingresar_usuario,
    show = "•"
)

documento_entry.place(x = 180, y = 200)


nombre_label = Label(
    Ingresar_usuario,
    text = "Nombre",
    borderwidth=0
)

nombre_label.configure(
    font = ("Bahnschrift", 12),
    fg="#FFFFFF",
    bg="#1E4024"
)

nombre_label.place(x = 208, y = 240)

nombre_entry = Entry(
    Ingresar_usuario,
)

nombre_entry.place(x = 180, y = 280)



fechaNacimiento_label = Label(
    Ingresar_usuario,
    text = "Fecha de Nacimiento",
    borderwidth=0
)

fechaNacimiento_label.configure(
    font = ("Bahnschrift", 12),
    fg="#FFFFFF",
    bg="#1E4024"
)

fechaNacimiento_label.place(x = 167, y = 320)

fechaNacimiento_entry = Entry(
    Ingresar_usuario
)

fechaNacimiento_entry.place(x = 180, y = 360)


#funcion que autocompleta a la hora de oprimir el document

def autocompletar(*args):
    documento_ingresado = documento_entry.get()
    with open("./Database/Usuarios.txt", "r") as archivo:
        lineas = archivo.readlines()
        for linea in lineas:
            datos_usuario = linea.split(",")
            documento = datos_usuario[3].strip() 
            if documento == documento_ingresado:
                nombre_entry.delete(0, END)
                nombre_entry.insert(0, datos_usuario[1])
                fechaNacimiento_entry.delete(0, END)
                fechaNacimiento_entry.insert(0, datos_usuario[2])
                break
        else:
            nombre_entry.delete(0, END)
            fechaNacimiento_entry.delete(0, END)
            
documento_entry.bind("<KeyRelease>", autocompletar)




Ingresar_usuario.mainloop()