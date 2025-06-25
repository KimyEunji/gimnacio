from db.db import conn

cursor = conn.cursor()

"""data = {
    "nombre"= "Juan",
    "correo"="Juan",
    "password"="Juan",
    "estado" ="Juan"
}"""

# la dunción recibe un diccionario y devuelve una tupla
# La tupla tiene 2 parametros, el primero el estado y el segundo el mensaje
        
def crear_socio(data):
    if not data["nombre"] or not data ["correo"] or not data ["password"] or not data ["estado"]:
        return (False, "es necesario enviar todos los parametros")
    cursor.execute("INSERT INTO socios(nombre,correo, password,estado) VALUES (%s,%s,%s,%s)",(data["nombre"],data["correo"],data["password"], data["estado"]))
    conn.commit()
    return (True, "sicio almacenado con exito")

##
def actualizar_socio(socio_id, data_udate):
    if not socio_id:
        return (False, "Es necesario enviar el ID de socio")
    
    query = "UPDATE socios SET=%s, correo=%s, password=%s, estado=%s WHERE id=%s"
    variables = (
        data_udate["name"],
        data_udate["email"],
        data_udate["password"],
        data_udate["state"],
        socio_id
    )
    cursor.execute(query, variables)
    conn.commit()
    return (True, "socio actualizado con exito")

#hhhh
def eliminar_socio(socio_id):
    query = "DELETE FROM socios WHERE id=%s"
    variable = (socio_id)
    cursor.execute(query, variable)
    conn.commit()
    return (True,"socio eliminado con exito")

 
def buscar_socio(socio_id):
    query = "SELECT * FROM socios WHERE id=%"
    variable = (socio_id)
    socio = cursor.fetchone
    if not socio:
        return(False, "no se encontro socio con ese id")
    return(True, socio)

def buscar_socios():
    query = "SELECT * FROM socios ORDER BY id"
    cursor.execute(query)
    socios = cursor.fetchall()
    return(True,socios)