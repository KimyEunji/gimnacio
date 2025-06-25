from db.db_init import iniciar_db
from views.main import ventana
from views.socios.crear_socio import mostrar_crear_socio

iniciar_db()
mostrar_crear_socio(ventana)
