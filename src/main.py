# Simulación de base de datos


def login(usuario, contraseña):
    # Simulación de usuarios válidos
    usuarios = {"admin@admin.com": "1234", "usuario@demo.com": "demo123"}
    return usuario in usuarios and usuarios[usuario] == contraseña


def agregar_al_carrito(carrito, id_producto):
    productos_disponibles = [1, 2, 3]
    if id_producto not in productos_disponibles:
        return carrito  # No se agrega nada
    pos = len(carrito) + 1
    carrito[pos] = {"posicion": pos, "id": id_producto}
    return carrito


def eliminar_del_carrito(carrito, pos):
    carrito.pop(pos, None)  # Elimina sin error si no existe
    return carrito


def guardar_comentario(comentario):
    # Simple validación para prevenir SQLi o XSS básico
    if any(peligroso in comentario for peligroso in ["<script>", "DROP", "SELECT", "--"]):
        return False
    return True