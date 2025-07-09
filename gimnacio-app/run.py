from db.db_init import iniciar_db
from views.main import ventana
from views.socios.home import mostrar_home_socios

iniciar_db()
mostrar_home_socios(ventana)
