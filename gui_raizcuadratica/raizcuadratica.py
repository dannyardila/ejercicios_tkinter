# se importa la librería tkinter con todas sus funciones
from tkinter import *
from tkinter import messagebox
import tkinter as tk

from requests import delete

# --------------------
# funciones de la app
# --------------------

def sumar():
    # messagebox.showinfo("Suma 1.0", "Hizo click en el boton sumar...")
    c = int(a.get()) + int(b.get())
    t_resultados.insert(INSERT, "La suma de " + a.get() + " + " + b.get() + " casi siempre es " + str(c)+"\n")

def borrar():
    messagebox.showinfo("Suma 1.0", "Los datos serán borrados...")
    a.set("")
    b.set("")
    t_resultados.delete("1.0","end")

def salir():
    messagebox.showinfo("Suma 1.0", "La app se cerrará...")
    ventana_principal.destroy()

# ------------------
# ventana principal
# ------------------

# se declara una variable llamada ventana_principal y que adquiere las caracteristicas de un objeto Tk()
ventana_principal = Tk()

# titulo de la ventana
ventana_principal.title("Raizces cuadraticas")

# establecer tamaño a la ventana
ventana_principal.geometry("800x500")

# icono de la ventana principal

ventana_principal.iconphoto(False, tk.PhotoImage(file='gui_raizcuadratica/bucara.png'))




# deshabilitar boton de maximar
ventana_principal.resizable(0,0)

# color de fondo de la ventana pricipal
ventana_principal.config(bg="black")

# -------------------
# variables globales
# -------------------
a = StringVar()
b = StringVar()
c = StringVar()
x1= IntVar()
x2= IntVar()

# ------------------
# frame entrada
# ------------------
frame_entrada = Frame(ventana_principal)
frame_entrada.config(bg="red", width=800, height=790)
frame_entrada.place(x=10,y=10)

# Etiqueta para el titulo de la app
titulo = Label(frame_entrada, text="Colegio San José de Guanentá")
titulo.config(bg="yellow", fg="blue", font=("Arial", 12))
titulo.place(x=8, y=4)

# Etiqueta para el subtitulo de la app
subtitulo = Label(frame_entrada, text="Especialidad en Sistemas")
subtitulo.config(bg="yellow", fg="blue", font=("Arial", 12))
subtitulo.place(x=390, y=10)

# Etiqueta para el subtitulo2 de la app
subtitulo2 = Label(frame_entrada, text="Raizces cuadraticas")
subtitulo2.config(bg="ivory2", fg="blue", font=("Arial", 12), anchor=CENTER)
subtitulo2.place(x=8, y=26)

# imagen - logo de la app
logo = PhotoImage(file="")
etiq_logo = Label(frame_entrada, image=logo)
etiq_logo.place(x=10,y=10)

# etiqueta para valor a
etiq_a = Label(frame_entrada, text="a = ")
etiq_a.config(bg="ivory2", fg="blue", font=("Arial", 20), anchor=CENTER)
etiq_a.place(x=5, y= 120)

# entry para el valor a
entry_a = Entry(frame_entrada, width=4, textvariable=a)
entry_a.config(font=("Arial", 20), justify=CENTER)
entry_a.focus_set()
entry_a.place(x=60,y=120)

# etiqueta para valor b
etiq_b = Label(frame_entrada, text="b = ")
etiq_b.config(bg="ivory2", fg="blue", font=("Arial", 20), anchor=CENTER)
etiq_b.place(x=160, y= 120)

# entry para el valor b
entry_b = Entry(frame_entrada, width=4, textvariable=b)
entry_b.config(font=("Arial", 20))
entry_b.place(x=150,y=120)

## entry para el valor c
entry_c = Entry(frame_entrada, width=4, textvariable=b)
entry_c.config(font=("Arial", 20))
entry_c.place(x=100,y=120)

# ------------------
# frame operaciones
# ------------------
frame_operaciones = Frame(ventana_principal)
frame_operaciones.config(bg="yellow", width=780, height=500)
frame_operaciones.place(x=400,y=10)

# boton para sumar los números - texto
bt_sum = PhotoImage(file="")
# bt_sumar = Button(frame_operaciones, text= "Sumar", width=10)
bt_sumar = Button(frame_operaciones, image=bt_sum, width=80, height=80, command=sumar)
bt_sumar.place(x=40, y=40)

# boton para borrar entradas y resultado
bt_bor = PhotoImage(file="")
# bt_borrar = Button(frame_operaciones, text="Borrar", width=10)
bt_borrar = Button(frame_operaciones, image=bt_bor, width=80, height=80, command=borrar)
bt_borrar.place(x=180, y=40)

# boton para salir - cerrar la app
bt_sal = PhotoImage(file="")
# bt_salir = Button(frame_operaciones, text="Salir", width=10)
bt_salir = Button(frame_operaciones, image=bt_sal, width=80, height=80, command=salir)
bt_salir.place(x=300, y=40)

# ------------------
# frame resultados
# ------------------
frame_resultados = Frame(ventana_principal)
frame_resultados.config(bg="blue", width=900, height=600)
frame_resultados.place(x=10,y=300)

# area de texto para resultados
t_resultados = Text(frame_resultados, width=260, height=19)
t_resultados.config(bg="blue", fg="white", font=("Courier", 16))
t_resultados.pack()

# se ejecuta el metodo mainloop() de la clase Tk() a través de la instancia ventana_principal.  Este metodo despliega una ventana simple en pantalla y queda a la espera de lo que el usuario haga (click en boton, escribir, etc).  Cada accion del usuario se conoce como un evento.  El metodo mainloop() es un bucle infinito.
ventana_principal.mainloop()
ventana_principal('wm', 'iconphoto', ventana_principal, PhotoImage(file='img/boton_borrar.png'))