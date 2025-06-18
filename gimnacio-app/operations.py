import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
from db_init import Database

class BaseWindow:
    def __init__(self, parent, db, title):
        self.window = tk.Toplevel(parent)
        self.window.title(title)
        self.window.geometry("800x600")
        
        self.db = db
        self.current_id = None
        
        # Frame principal
        main_frame = tk.Frame(self.window)
        main_frame.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)
        
        # Formulario
        form_frame = tk.Frame(main_frame)
        form_frame.pack(fill=tk.X, pady=5)
        self.create_form(form_frame)
        
        # Botones
        button_frame = tk.Frame(main_frame)
        button_frame.pack(fill=tk.X, pady=5)
        self.create_buttons(button_frame)
        
        # Tabla
        table_frame = tk.Frame(main_frame)
        table_frame.pack(expand=True, fill=tk.BOTH)
        self.create_table(table_frame)
        
        self.load_data()
    
    def create_form(self, frame):
        # Implementar en clases hijas
        pass
    
    def create_buttons(self, frame):
        tk.Button(frame, text="Guardar", command=self.save).pack(side=tk.LEFT, padx=5)
        tk.Button(frame, text="Limpiar", command=self.clear).pack(side=tk.LEFT, padx=5)
        tk.Button(frame, text="Eliminar", command=self.delete).pack(side=tk.LEFT, padx=5)
    
    def create_table(self, frame):
        self.tree = ttk.Treeview(frame)
        scroll_y = ttk.Scrollbar(frame, orient="vertical", command=self.tree.yview)
        scroll_x = ttk.Scrollbar(frame, orient="horizontal", command=self.tree.xview)
        
        self.tree.configure(yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        scroll_y.pack(side=tk.RIGHT, fill=tk.Y)
        scroll_x.pack(side=tk.BOTTOM, fill=tk.X)
        
        self.tree.bind("<<TreeviewSelect>>", self.on_select)
    
    def on_select(self, event):
        item = self.tree.focus()
        if item:
            self.current_id = self.tree.item(item, "values")[0]
            self.fill_form(self.tree.item(item, "values"))
    
    def fill_form(self, values):
        # Implementar en clases hijas
        pass
    
    def clear(self):
        self.current_id = None
        for widget in self.window.winfo_children():
            if isinstance(widget, tk.Entry):
                widget.delete(0, tk.END)
            elif isinstance(widget, ttk.Combobox):
                widget.set("")
    
    def load_data(self):
        # Implementar en clases hijas
        pass
    
    def save(self):
        # Implementar en clases hijas
        pass
    
    def delete(self):
        if not self.current_id:
            messagebox.showwarning("Advertencia", "Seleccione un registro")
            return
        
        if messagebox.askyesno("Confirmar", "¿Eliminar este registro?"):
            try:
                cursor = self.db.connection.cursor()
                cursor.execute(f"DELETE FROM {self.table} WHERE id = %s", (self.current_id,))
                self.db.connection.commit()
                messagebox.showinfo("Éxito", "Registro eliminado")
                self.clear()
                self.load_data()
            except Exception as e:
                self.db.connection.rollback()
                messagebox.showerror("Error", f"No se pudo eliminar: {str(e)}")

class SociosWindow(BaseWindow):
    def __init__(self, parent, db):
        self.table = "socios"
        super().__init__(parent, db, "Socios")
    
    def create_form(self, frame):
        tk.Label(frame, text="Nombre:").grid(row=0, column=0, padx=5, pady=5)
        self.nombre = tk.Entry(frame, width=30)
        self.nombre.grid(row=0, column=1, padx=5, pady=5)
        
        tk.Label(frame, text="Email:").grid(row=1, column=0, padx=5, pady=5)
        self.email = tk.Entry(frame, width=30)
        self.email.grid(row=1, column=1, padx=5, pady=5)
    
    def load_data(self):
        self.tree["columns"] = ("id", "nombre", "email")
        
        self.tree.column("#0", width=0, stretch=tk.NO)
        self.tree.column("id", width=50, anchor=tk.CENTER)
        self.tree.column("nombre", width=200, anchor=tk.W)
        self.tree.column("email", width=250, anchor=tk.W)
        
        self.tree.heading("id", text="ID")
        self.tree.heading("nombre", text="Nombre")
        self.tree.heading("email", text="Email")
        
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        try:
            cursor = self.db.connection.cursor()
            cursor.execute("SELECT id, nombre, email FROM socios")
            for row in cursor.fetchall():
                self.tree.insert("", tk.END, values=row)
        except Exception as e:
            messagebox.showerror("Error", f"No se pudieron cargar los datos: {str(e)}")
    
    def save(self):
        nombre = self.nombre.get().strip()
        email = self.email.get().strip()
        
        if not nombre or not email:
            messagebox.showwarning("Advertencia", "Complete todos los campos")
            return
        
        try:
            cursor = self.db.connection.cursor()
            if self.current_id:
                cursor.execute(
                    "UPDATE socios SET nombre = %s, email = %s WHERE id = %s",
                    (nombre, email, self.current_id)
            else:
                cursor.execute(
                    "INSERT INTO socios (nombre, email) VALUES (%s, %s)",
                    (nombre, email))
            
            self.db.connection.commit()
            self.clear()
            self.load_data()
        except Exception as e:
            self.db.connection.rollback()
            messagebox.showerror("Error", f"No se pudo guardar: {str(e)}")

class EntrenadoresWindow(BaseWindow):
    def __init__(self, parent, db):
        self.table = "entrenadores"
        super().__init__(parent, db, "Entrenadores")
    
    def create_form(self, frame):
        tk.Label(frame, text="Nombre:").grid(row=0, column=0, padx=5, pady=5)
        self.nombre = tk.Entry(frame, width=30)
        self.nombre.grid(row=0, column=1, padx=5, pady=5)
        
        tk.Label(frame, text="Especialidad:").grid(row=1, column=0, padx=5, pady=5)
        self.especialidad = tk.Entry(frame, width=30)
        self.especialidad.grid(row=1, column=1, padx=5, pady=5)
    
    def load_data(self):
        self.tree["columns"] = ("id", "nombre", "especialidad")
        
        self.tree.column("#0", width=0, stretch=tk.NO)
        self.tree.column("id", width=50, anchor=tk.CENTER)
        self.tree.column("nombre", width=200, anchor=tk.W)
        self.tree.column("especialidad", width=200, anchor=tk.W)
        
        self.tree.heading("id", text="ID")
        self.tree.heading("nombre", text="Nombre")
        self.tree.heading("especialidad", text="Especialidad")
        
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        try:
            cursor = self.db.connection.cursor()
            cursor.execute("SELECT id, nombre, especialidad FROM entrenadores")
            for row in cursor.fetchall():
                self.tree.insert("", tk.END, values=row)
        except Exception as e:
            messagebox.showerror("Error", f"No se pudieron cargar los datos: {str(e)}")
    
    def save(self):
        nombre = self.nombre.get().strip()
        especialidad = self.especialidad.get().strip()
        
        if not nombre or not especialidad:
            messagebox.showwarning("Advertencia", "Complete todos los campos")
            return
        
        try:
            cursor = self.db.connection.cursor()
            if self.current_id:
                cursor.execute(
                    "UPDATE entrenadores SET nombre = %s, especialidad = %s WHERE id = %s",
                    (nombre, especialidad, self.current_id))
            else:
                cursor.execute(
                    "INSERT INTO entrenadores (nombre, especialidad) VALUES (%s, %s)",
                    (nombre, especialidad))
            
            self.db.connection.commit()
            self.clear()
            self.load_data()
        except Exception as e:
            self.db.connection.rollback()
            messagebox.showerror("Error", f"No se pudo guardar: {str(e)}")