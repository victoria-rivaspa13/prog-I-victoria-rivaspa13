menu = [
    # ID, NAME, PRICE, AVAILABLE, TIMES_ORDERED
    [1, "Pizza Margherita", 800, True, 5],
    [2, "Pasta Alfredo", 700, True, 10],
]

clientes = [
    # DNI, NAME, ORDERS, PAYMENTS
    [12345678, "Alice", 3, 2400],
    [98765432, "Bob", 1, 700],
]

ordenes = [
    # ORDER_ID, DNI, ITEM_ID, ORDER_DATE
    [1001, 12345678, 1, "2024-12-01"],
]

pagos = [
    # PAYMENT_ID, DNI, AMOUNT, PAYMENT_DATE
    [5001, 98765432, 700, "2024-11-29"],
]

def añadir_plato(ID, nombre, precio):
    menu = []
    menu.append([ID, nombre, precio, True, 0])

def listar_menu(menu):
    for plato in menu:
        if plato[3]:
            print(f"ID: {plato[0]}, Name: {plato[1]}, Precio: ${plato[2]}")

def ordenar(dni, id_plato, fecha):
    cliente_encontrado = None
    plato_encontrado = None

    for cliente in clientes:
        if cliente[0] == dni:
            cliente_encontrado = cliente

    for plato in menu:
        if plato[0]:
            if plato[0] == id_plato:
                plato_encontrado = plato

    if not cliente_encontrado or not plato_encontrado:
        return f"Imposible encontrar data para el ITEM ID: {id_plato} y DNI: {dni}"

    if not plato_encontrado[3]:
        return f"Plato ID: {id_plato} no disponible"

    plato_encontrado[3] = False
    plato_encontrado[4] += 1
    ordenes.append([len(ordenes) + 1, dni, id_plato, fecha])
    return f"Usuario {dni} ordenó el pedido {id_plato}"

def registrar_pago(dni, monto, fecha):
    cliente_encontrado = None
    for cliente in clientes:
        if cliente[0] == dni:
            cliente_encontrado = cliente

        if not cliente_encontrado:
            return f"Imposible encontrar un cliente con DNI: {dni}"

        cliente_encontrado[3] += monto
        pagos.append([len(pagos) + 1, dni, monto, fecha])

