import tkinter as tk
from tkinter import messagebox as mb
from views.resources import PRIMARY_COLOR, SECONDARY_COLOR, THIRD_COLOR, TITLES, TEXTS

def mostrar_crear_socio(ventana):
    # Borrar lo que habia antes 
    for widget in ventana.winfo_children():
        widget.destroy()
    # Inicio de Ventana para crear socios 
    for i in range(9):
        ventana.rowconfigure(i, weight=1)
    ventana.columconfigure(0, weight=1)
    ventana.columconfigure(1)
    ventana.columconfigure(2, weight=1)

    tk.Label(ventana, text="Crear Socio", bg=PRIMARY_COLOR, font=TITLES, fg=SECONDARY_COLOR)

    