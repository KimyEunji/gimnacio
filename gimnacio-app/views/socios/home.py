import tkinter as tk 
from views.resources import PRIMARY_COLOR, SECONDARY_COLOR, THIRD_COLOR, FOURTH_COLOR, TITLES, SUBTITLES, TEXTS, LOGO
from views.socios.crear_socio import mostrar_crear_socio
from db.operations import buscar_socios
from PIL import Image, ImageTk

def mostrar_home_socios(w:tk.Tk):
    for widget in w.winfo_children():
        widget.destroy()

    for i in range(7):
        w.rowconfigure(i, weight=1)
        w.columnconfigure(i, weight=1)

    # Logo
    image_pil = Image.open(LOGO)
    resized_image = image_pil.resize((100,100))
    photo = ImageTk.PhotoImage(image_pil)
    w.photo = photo
    tk.Label(image=photo).grid(row=0, column=0, columnspan=7, sticky="n")

    # Menu de navegacion
    buttons_labels = ["Socios", "Membresias", "Entrenadores"]
    for indice, buttons_label in enumerate(buttons_labels, 2):
        tk.Button(text=buttons_label, font=TITLES, bg=THIRD_COLOR, fg=SECONDARY_COLOR, relief="groove"). grid(column=indice, row=1, sticky="we")
   
   # Sutitulo y crear nuevo socio 
    tk.Label(text="Socios", font=TITLES, bg=PRIMARY_COLOR, fg=SECONDARY_COLOR).grid(column=0, row=2, sticky="n", columnspan=7)
    tk.Button(text="Crear Socio", font=TEXTS, bg=THIRD_COLOR, fg=SECONDARY_COLOR, command=lambda:mostrar_crear_socio(w), relief="groove").grid(column=4, row=2)

    w.mainloop()