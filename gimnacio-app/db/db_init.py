from db.db import conn

#Para que no esten vacios se utiliza el NOT NULL
#Varchar es para guardar taxto
sql_schema = """
CREATE TABLE iF NOT EXISTS socios(
   id SERIAL PRIMARY KEY,
   nombre VARCHAR(100) NOT NULL,    
   correo VARCHAR(50) NOT NULL,
   password VARCHAR(100) NOT NULL,
   estado VARCHAR(50) NOT NULL
   );

CREATE TABLE IF NOT EXISTS membresias(
   id SERIAL PRIMARY KEY,
   nombre VARCHAR(100) NOT NULL,
   preicio NUMERIC(10,2) NOT NULL
   );  

CREATE TABLE iF NOT EXISTS entrenadores(
   id SERIAL PRIMARY KEY,
   nombre VARCHAR(100) NOT NULL,    
   correo VARCHAR(50) NOT NULL,
   password VARCHAR(100) NOT NULL
   );
"""

def iniciar_db():
    try:
        cursor = conn.cursor()
        cursor.execute(sql_schema)
        conn.commit()
        print("tabla crada con exito :P")
    except Exception as e:
        print("Error ocurrido: ", e)

iniciar_db()