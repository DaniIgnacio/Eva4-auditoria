from src.main import login, agregar_al_carrito, eliminar_del_carrito, guardar_comentario


# ---------- PRUEBAS DE LOGIN ----------
def test_login_correcto():
    assert login("admin@admin.com", "1234") is True

def test_login_usuario_incorrecto():
    assert login("hacker@fake.com", "1234") is False

def test_login_contraseña_incorrecta():
    assert login("admin@admin.com", "wrong") is False

def test_login_ambos_incorrectos():
    assert login("wrong", "wrong") is False


# ---------- PRUEBAS DE CARRITO ----------
def test_agregar_producto_valido():
    carrito = {}
    nuevo_carrito = agregar_al_carrito(carrito, 1)
    assert 1 in [item["id"] for item in nuevo_carrito.values()]

def test_agregar_producto_invalido():
    carrito = {}
    nuevo_carrito = agregar_al_carrito(carrito, 99)
    assert len(nuevo_carrito) == 0

def test_eliminar_producto_existente():
    carrito = {1: {"posicion": 1, "id": 1}}
    actualizado = eliminar_del_carrito(carrito, 1)
    assert 1 not in actualizado

def test_eliminar_producto_inexistente():
    carrito = {1: {"posicion": 1, "id": 1}}
    actualizado = eliminar_del_carrito(carrito, 99)
    assert 1 in actualizado


# ---------- PRUEBAS DE COMENTARIOS ----------
def test_comentario_valido():
    comentario = "Muy buena atención."
    assert guardar_comentario(comentario) is True

def test_comentario_con_script():
    comentario = "<script>alert('XSS')</script>"
    assert guardar_comentario(comentario) is False

def test_comentario_con_sql():
    comentario = "'); DROP TABLE usuarios; --"
    assert guardar_comentario(comentario) is False