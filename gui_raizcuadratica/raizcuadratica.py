# se importa la librería tkinter con todas sus funciones
from tkinter import *
from tkinter import messagebox
import tkinter as tk
import math
from cmath import sqrt
from requests import delete
from tkinter import font


# --------------------
# funciones de la app
# --------------------

def calcular():
    d=int(b.get())**2-4*int(a.get())*int(c.get())
    
    if d>0:
        x1=(-int(b.get())+math.sqrt(d))/(2*int(a.get()))
        x2=(-int(b.get())-math.sqrt(d))/(2*int(a.get()))
        t_resultados.insert(INSERT, "x1="+str(x1)+ "\nx2="+str(x2)+ "\n Son dos raíces distintas")
    elif d==0:
        x1=-int(b.get())/2*int(a.get())
        x2=x1
        t_resultados.insert(INSERT, "x1="+str(x1)+"\nx2="+str(x2)+ "\nx1 y x2  iguales \n Son dos raíces reales distintas")
    else:
        t_resultados.insert(INSERT,"Es parte de las raíces imaginarias o complejas.\n No hay solución en los números reales" )

def borrar():
    messagebox.showinfo("Suma 1.0", "Los datos serán borrados...")
    a.set("")
    b.set("")
    c.set("")
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

ventana_principal.iconphoto(False, tk.PhotoImage(file='gui_raizcuadratica/city.png'))




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
d = IntVar()
x1= IntVar()
x2= IntVar()

# ------------------
# frame entrada
# ------------------
frame_entrada = Frame(ventana_principal)
frame_entrada.config(bg="white", width=800, height=790)
frame_entrada.place(x=10,y=10)

# Etiqueta para el titulo de la app
titulo = Label(frame_entrada, text="Colegio San José de Guanentá")
titulo.config(bg="white", fg="black", font=("Arial", 12))
titulo.place(x=8, y=4)

# Etiqueta para el subtitulo de la app
subtitulo = Label(frame_entrada, text="Especialidad en Sistemas")
subtitulo.config(bg="white", fg="black", font=("Arial", 12))
subtitulo.place(x=8, y=50)

# Etiqueta para el subtitulo2 de la app
subtitulo2 = Label(frame_entrada, text="Raices cuadraticas")
subtitulo2.config(bg="white", fg="black", font=("Arial", 12), anchor=CENTER)
subtitulo2.place(x=8, y=26)

# imagen - logo de la app
logo = PhotoImage(file="")
etiq_logo = Label(frame_entrada, image=logo)
etiq_logo.place(x=10,y=10)

# etiqueta para valor a
etiq_a = Label(frame_entrada, text="a = ")
etiq_a.config(bg="white", fg="black", font=("Arial", 20), anchor=CENTER)
etiq_a.place(x=5, y= 120)

# entry para el valor a
entry_a = Entry(frame_entrada, width=4, textvariable=a)
entry_a.config(font=("Arial", 20), justify=CENTER)
entry_a.focus_set()
entry_a.place(x=60,y=120)

# etiqueta para valor b
etiq_b = Label(frame_entrada, text="b = ")
etiq_b.config(bg="white", fg="black", font=("Arial", 20), anchor=CENTER)
etiq_b.place(x=130, y= 120)

# entry para el valor b
entry_b = Entry(frame_entrada, width=4, textvariable=b)
entry_b.config(font=("Arial", 20))
entry_b.place(x=185,y=120)

# etiqueta para valor c
etiq_c = Label(frame_entrada, text="c = ")
etiq_c.config(bg="white", fg="black", font=("Arial", 20), anchor=CENTER)
etiq_c.place(x=260, y= 120)



## entry para el valor c
entry_c = Entry(frame_entrada, width=4, textvariable=c)
entry_c.config(font=("Arial", 20))
entry_c.place(x=313,y=120)

# ------------------
# frame operaciones
# ------------------
frame_operaciones = Frame(ventana_principal)
frame_operaciones.config(bg="white", width=780, height=500)
frame_operaciones.place(x=400,y=10)

# boton para sumar los números - texto
bt_sum = PhotoImage(file="gui_raizcuadratica/raiz2.png")
# bt_sumar = Button(frame_operaciones, text= "Sumar", width=10)
bt_sumar = Button(frame_operaciones, image=bt_sum, width=80, height=80, command=calcular)
bt_sumar.place(x=70, y=70)

# boton para borrar entradas y resultado
bt_bor = PhotoImage(file="gui_raizcuadratica/borrar2.png")
# bt_borrar = Button(frame_operaciones, text="Borrar", width=10)
bt_borrar = Button(frame_operaciones, image=bt_bor, width=80, height=80, command=borrar)
bt_borrar.place(x=180, y=70)

# boton para salir - cerrar la app
bt_sal = PhotoImage(file="gui_raizcuadratica/salir1.png")
# bt_salir = Button(frame_operaciones, text="Salir", width=10)
bt_salir = Button(frame_operaciones, image=bt_sal, width=80, height=80, command=salir)
bt_salir.place(x=300, y=70)

# ------------------
# frame resultados
# ------------------
frame_resultados = Frame(ventana_principal)
frame_resultados.config(bg="black", width=900, height=600)
frame_resultados.place(x=10,y=300)

# area de texto para resultados
t_resultados = Text(frame_resultados, width=65, height=19)
t_resultados.config(bg="black", fg="white", font=("Courier", 16))
t_resultados.pack()

# se ejecuta el metodo mainloop() de la clase Tk() a través de la instancia ventana_principal.  Este metodo despliega una ventana simple en pantalla y queda a la espera de lo que el usuario haga (click en boton, escribir, etc).  Cada accion del usuario se conoce como un evento.  El metodo mainloop() es un bucle infinito.
ventana_principal.mainloop()
ventana_principal('wm', 'iconphoto', ventana_principal, PhotoImage(file='img/boton_borrar.png'))