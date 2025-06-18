import psycopg2
from tkinter import messagebox

# Configuración de la base de datos
DB_CONFIG = {
    "dbname": "gimnacio",
    "user": "postgres",
    "password": "42001217",
    "host": "localhost",
    "port": "5432"
}

class Database:
    def __init__(self):
        self.connection = None
    
    def connect(self):
        try:
            self.connection = psycopg2.connect(**DB_CONFIG)
            self.create_tables()
            return True
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo conectar a la base de datos:\n{str(e)}")
            return False
    
    def create_tables(self):
        drop_tables_sql = """
        DROP TABLE IF EXISTS inscripciones CASCADE;
        DROP TABLE IF EXISTS asistencias CASCADE;
        DROP TABLE IF EXISTS pagos CASCADE;
        DROP TABLE IF EXISTS clases CASCADE;
        DROP TABLE IF EXISTS membresias CASCADE;
        DROP TABLE IF EXISTS entrenadores CASCADE;
        DROP TABLE IF EXISTS socios CASCADE;
        DROP TABLE IF EXISTS roles CASCADE;
        """
        
        create_tables_sql = """
        CREATE TABLE IF NOT EXISTS roles(
            id_rol SERIAL PRIMARY KEY,
            nombre VARCHAR(50) NOT NULL
        );
        
        CREATE TABLE IF NOT EXISTS socios(
            id_socio SERIAL PRIMARY KEY,
            nombre VARCHAR(100) NOT NULL,
            email VARCHAR(100) UNIQUE NOT NULL,
            estado VARCHAR(20) NOT NULL
        );
        
        CREATE TABLE IF NOT EXISTS entrenadores(
            id_entrenador SERIAL PRIMARY KEY,
            nombre VARCHAR(100) NOT NULL,
            email VARCHAR(100) UNIQUE NOT NULL
        );
        
        CREATE TABLE IF NOT EXISTS membresias(
            id_membresia SERIAL PRIMARY KEY,
            nombre VARCHAR(100) NOT NULL,
            precio DECIMAL(10,2) NOT NULL
        );
        
        CREATE TABLE IF NOT EXISTS clases(
            id_clase SERIAL PRIMARY KEY,
            nombre VARCHAR(100) NOT NULL,
            id_entrenador INTEGER REFERENCES entrenadores(id_entrenador),
            cupos_maximos INTEGER NOT NULL,
            horario TIME NOT NULL
        );
        
        CREATE TABLE IF NOT EXISTS pagos(
            id_pago SERIAL PRIMARY KEY,
            id_socio INTEGER REFERENCES socios(id_socio),
            id_membresia INTEGER REFERENCES membresias(id_membresia),
            monto DECIMAL(10,2) NOT NULL,
            fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            metodo_pago VARCHAR(50) NOT NULL
        );
        
        CREATE TABLE IF NOT EXISTS asistencias(
            id_asistencia SERIAL PRIMARY KEY,
            id_socio INTEGER REFERENCES socios(id_socio),
            fecha_entrada TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        
        CREATE TABLE IF NOT EXISTS inscripciones(
            id_inscripcion SERIAL PRIMARY KEY,
            id_socio INTEGER REFERENCES socios(id_socio),
            id_clase INTEGER REFERENCES clases(id_clase),
            fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        
        INSERT INTO roles (nombre) VALUES ('Administrador'), ('Entrenador'), ('Socio')
        ON CONFLICT DO NOTHING;
        """
        
        try:
            cursor = self.connection.cursor()
            cursor.execute(drop_tables_sql)
            self.connection.commit()
            
            cursor.execute(create_tables_sql)
            self.connection.commit()
            cursor.close()
            messagebox.showinfo("Éxito", "Tablas creadas correctamente")
        except Exception as e:
            self.connection.rollback()
            messagebox.showerror("Error", f"Error al crear tablas:\n{str(e)}")
            raise e

    def get_entrenadores(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT id_entrenador, nombre FROM entrenadores ORDER BY nombre")
            result = cursor.fetchall()
            cursor.close()
            return result
        except Exception as e:
            messagebox.showerror("Error", f"Error al obtener entrenadores:\n{str(e)}")
            return []

    def get_socios(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT id_socio, nombre FROM socios ORDER BY nombre")
            result = cursor.fetchall()
            cursor.close()
            return result
        except Exception as e:
            messagebox.showerror("Error", f"Error al obtener socios:\n{str(e)}")
            return []

    def get_membresias(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT id_membresia, nombre, precio FROM membresias ORDER BY nombre")
            result = cursor.fetchall()
            cursor.close()
            return result
        except Exception as e:
            messagebox.showerror("Error", f"Error al obtener membresías:\n{str(e)}")
            return []

    def get_clases(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
                SELECT c.id_clase, c.nombre, e.nombre 
                FROM clases c
                JOIN entrenadores e ON c.id_entrenador = e.id_entrenador
                ORDER BY c.nombre
            """)
            result = cursor.fetchall()
            cursor.close()
            return result
        except Exception as e:
            messagebox.showerror("Error", f"Error al obtener clases:\n{str(e)}")
            return []