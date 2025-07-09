import tkinter as tk
from views.resources import ICON, PRIMARY_COLOR

ventana = tk.Tk()
ventana.configure(background=PRIMARY_COLOR)
ventana.iconbitmap(ICON)
ventana.state("zoomed")
