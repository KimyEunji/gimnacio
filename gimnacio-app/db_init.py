import psycopg2 as psq

# Configuración de la base de datos
DB_CONFIG = {
    "dbname": "gimnacio",
    "user": "postgres",
    "password": "42001217",
    "host": "localhost",
    "port": "5432"
}

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
   id SERIAL PRIMARY KEY
   nombre VARCHAR(100) NOT NULL,
   preicio VARCHAR(10,2) NOT NULL
   )  

CREATE TABLE iF NOT EXISTS entrenadores(
   id SERIAL PRIMARY KEY,
   nombre VARCHAR(100) NOT NULL,    
   correo VARCHAR(50) NOT NULL,
   password VARCHAR(100) NOT NULL
   );
"""

def iniciar_db():
    try:
        conn = psq.connect(
            dbname = DB_NAME,
            user = DB_USER,
            passwird = DB_PASSWORD,
            host = DB_HOST,
            port = DB_PORT
        )
        cursor = conn.cursor()
        cursor.execute(sql_schema)
        conn.commit()
        print("tabla crada con exito :P")
    except Exception as e:
        print("Error ocurrido: ", e)